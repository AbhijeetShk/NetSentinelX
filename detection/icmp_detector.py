
def detect_icmp_flood(packet, count):

    try:
        if packet.haslayer("ICMP"):

            if count > 60:
                return "ICMP Flood Detected"

    except:
        pass

    return None
