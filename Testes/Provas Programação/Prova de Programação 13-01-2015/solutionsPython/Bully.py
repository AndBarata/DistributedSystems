import socket
import sys
import time

class Bully():
    def __init__(self, host, port, id, T, delay):

        self.id = int(id)
        self.T = float(T) # em milissegundos
        self.delay = float(delay) * self.id
        self.state = "idle"

        self.host = str(host)
        self.port = int(port + self.id)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        
    def send(self, data):
        self.sock.sendto(data.encode("utf-8"), (self.host, self.port))

    def receive(self):
        data, addr = self.sock.recvfrom(1024)
        if data:
            print(f"FROM {addr} | data")
            return data.decode("utf-8"), addr




if len(sys.argv) != 6:
    print("Usage: python3 Bully.py <addr> <port> <id> <T> <delay>")
    sys.exit()
bully = Bully(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

while True:
    time.sleep(bully.delay)
    bully.send(str(bully.id))
    data, addr = bully.receive()