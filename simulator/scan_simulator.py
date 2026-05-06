
import socket

target = "127.0.0.1"

print("Starting Port Scan Simulation...")

for port in range(1, 1000):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)

    try:
        s.connect((target, port))

    except:
        pass

    s.close()

print("Scan completed.")
