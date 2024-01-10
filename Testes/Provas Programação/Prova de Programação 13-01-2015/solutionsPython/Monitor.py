import socket
import threading
import time
import sys

class Monitor():
    def __init__(self, addr, port, period, timeout):
        self.host = str(addr)
        self.port = int(port)
        self.pingPeriod = float(period)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(float(period))
        self.sock.bind((self.host, self.port))
        self.sock.listen()

    def send(self, data, addr, conn):
        conn.sendall(data.encode("utf-8"))
        print(f"MONITOR to {addr} | {data}")

    def receive(self, addr, conn):
        try:
            data = conn.recv(1024).decode("utf-8")
            print(f"MONITOR from {addr} | {data}")
            return data

        except self.sock.timeout:
            print(f"MONITOR | Fail to ping {addr}")
        

    def handleConnection(self, addr, conn):
        while True:
            self.send("ping", addr, conn)
            self.receive(addr, conn)
            time.sleep(self.pingPeriod)

    def start(self):
        while True:
            try:
                conn, addr = self.sock.accept()
            except:
                continue
            print(f"MONITOR | New connection with {addr}")
            threading.Thread(target = self.handleConnection, args=(addr, conn)).start()

if len(sys.argv) != 5:
    print("Argument error. python3 Monitor.py <addr> <port> <period> <timeout>")
    sys.exit()

monitor = Monitor(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
monitor.start()
