
def detect_port_scan(packet, count):

    try:
        if packet.haslayer("TCP"):

            if count > 80:
                return "Possible Port Scan"

    except:
        pass

    return None
