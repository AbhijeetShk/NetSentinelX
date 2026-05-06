
def recommendation(alert):

    actions = {
        "Possible SYN Flood":
            "Block IP and inspect firewall logs.",

        "Possible Port Scan":
            "Investigate scanning source and close unnecessary ports.",

        "ICMP Flood Detected":
            "Limit ICMP requests using firewall rules.",

        "Normal":
            "No action required."
    }

    return actions.get(alert, "Monitor activity.")
