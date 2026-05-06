
import socket
import threading

active_hosts = []

def scan(ip):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((ip, 80))
        active_hosts.append(ip)
        print(f"[ACTIVE] {ip}")

    except:
        pass

base_ip = "192.168.1."

threads = []

for i in range(1, 255):

    ip = base_ip + str(i)

    t = threading.Thread(target=scan, args=(ip,))

    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nDiscovered Devices:")

for host in active_hosts:
    print(host)
