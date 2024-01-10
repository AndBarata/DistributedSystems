import socket
import time
import sys


class Client():
    def __init__(self, addr, port):
        self.host = str(addr)
        self.port = int(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(5.0)

    def send(self, data):
        self.sock.sendto(data.encode("utf-8"), (self.host, self.port))

    def receive(self):
        try:
            data, addr = self.sock.recvfrom(1024)
        except self.sock.timeout:
            print("CLIENT | TIMEOUT") 
            return None           
            
        return data.decode("utf-8"), addr


if len(sys.argv) != 3:
    print("Error in arguments. python3 Client.py <addr> <port>")
    sys.exit()

client = Client(sys.argv[1], sys.argv[2])


while True:
    client.send("REQ average")
    print(f"TX_CLIENT | REQ average")
    data, addr = client.receive()
    print(f"RX_CLIENT | {data}")
    time.sleep(1)
