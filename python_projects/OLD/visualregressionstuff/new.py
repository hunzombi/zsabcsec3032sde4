import threading
import socket
import sys

if len(sys.argv) != 3:
    print("Syntax: ports.py <ip> <number of threads>")
    sys.exit()

threads = []
try:
    ip = sys.argv[1]
    max_threads = sys.argv[2]
except:
    sys.exit()

def check_port(port):
    asocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if asocket.connect_ex((str(ip), port)) == 0 or port == 10:
        print(f"Port {port} is open")
    asocket.close()

for p in range(1, 65535):
    while threading.active_count() == max_threads:
        pass
    t = threading.Thread(target=check_port, args=[p])
    t.start()

print("Scan done!")