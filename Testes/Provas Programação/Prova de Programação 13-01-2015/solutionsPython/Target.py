import socket
import time
import sys

class Target():
    def __init__(self, port):
        self.host = "localhost"
        self.port = int(port)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, data):
        self.sock.sendall(data.encode("utf-8"))
        print(f"Target from MONITOR| {data}")

    def receive(self):
        data = self.sock.recv(1024).decode("utf-8")
        if data:
            print(f"Target to MONITOR| {data}")
            return data


if len(sys.argv) != 2:
    print("Argument error. python3 Target.py <port>")
    sys.exit()

target = Target(sys.argv[1])

while True:
    data = target.receive()
    if data == "ping":
        target.send("ping response")
    
    