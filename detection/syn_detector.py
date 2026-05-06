
def detect_syn_flood(packet, count):

    try:
        if packet.haslayer("TCP"):

            flags = packet["TCP"].flags

            if flags == "S" and count > 100:
                return "Possible SYN Flood"

    except:
        pass

    return None
