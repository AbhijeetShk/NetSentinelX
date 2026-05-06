
def calculate_risk(alert):

    scores = {
        "Possible SYN Flood": 92,
        "Possible Port Scan": 76,
        "ICMP Flood Detected": 81,
        "Normal": 5
    }

    return scores.get(alert, 20)
