import socket
import sys
import time

class Client():
    def __init__(self, addr, port):
        self.host = str(addr)
        self.port = int(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.connect((self.host, self.port))

    def send(self, data):
        self.sock.sendall(data.encode("utf-8"))

    def receive(self):
        return self.sock.recv(1024).decode("utf-8")



if len(sys.argv) != 3:
    print("Error in arguments. python3 Client.py <addr> <port>")
    sys.exit()

client = Client(sys.argv[1], sys.argv[2])

while True:
    client.send("REQ average")
    print("TX_CLIENT | REQ average")
    response = client.receive()
    if response:
        print(f"RX_CLIENT_RX | {response}")

    time.sleep(1.0)
    