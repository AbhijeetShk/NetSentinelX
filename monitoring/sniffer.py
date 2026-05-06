import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
from scapy.all import sniff
from collections import defaultdict
from datetime import datetime

import pandas as pd

from detection.syn_detector import detect_syn_flood
from detection.portscan_detector import detect_port_scan
from detection.icmp_detector import detect_icmp_flood

from threat_intelligence.scorer import calculate_risk
from threat_intelligence.recommender import recommendation
Path("alerts").mkdir(exist_ok=True)

ALERT_FILE = "alerts/alerts.csv"

if not Path(ALERT_FILE).exists():
    pd.DataFrame(columns=[
        "timestamp",
        "src_ip",
        "dst_ip",
        "protocol",
        "alert",
        "severity",
        "risk_score",
        "recommendation"
    ]).to_csv(ALERT_FILE, index=False)

traffic_counter = defaultdict(int)

def classify_protocol(packet):

    if packet.haslayer("TCP"):
        port = packet["TCP"].dport

        mapping = {
            80: "HTTP",
            443: "HTTPS",
            22: "SSH",
            21: "FTP",
            25: "SMTP",
            53: "DNS"
        }

        return mapping.get(port, "TCP")

    if packet.haslayer("UDP"):
        return "UDP"

    if packet.haslayer("ICMP"):
        return "ICMP"

    return "OTHER"

def process_packet(packet):

    try:
        if packet.haslayer("IP"):

            src = packet["IP"].src
            dst = packet["IP"].dst

            traffic_counter[src] += 1

            protocol = classify_protocol(packet)

            alerts = []

            syn = detect_syn_flood(packet, traffic_counter[src])
            if syn:
                alerts.append(syn)

            scan = detect_port_scan(packet, traffic_counter[src])
            if scan:
                alerts.append(scan)

            icmp = detect_icmp_flood(packet, traffic_counter[src])
            if icmp:
                alerts.append(icmp)

            if not alerts:
                alerts.append("Normal")

            for alert in alerts:

                risk = calculate_risk(alert)

                severity = "LOW"

                if risk > 80:
                    severity = "CRITICAL"
                elif risk > 60:
                    severity = "HIGH"
                elif risk > 30:
                    severity = "MEDIUM"

                row = {
                    "timestamp": datetime.now(),
                    "src_ip": src,
                    "dst_ip": dst,
                    "protocol": protocol,
                    "alert": alert,
                    "severity": severity,
                    "risk_score": risk,
                    "recommendation": recommendation(alert)
                }

                pd.DataFrame([row]).to_csv(
                    ALERT_FILE,
                    mode="a",
                    header=False,
                    index=False
                )

                print(row)

    except Exception as e:
        print(e)

print("[*] NetSentinelX Threat Engine Running...")

sniff(prn=process_packet, store=False)
