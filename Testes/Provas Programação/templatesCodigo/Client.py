import socket
import time

class Client():
    def __init__(self):
        self.host = "localhost"
        self.port = 33001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, data):
        self.sock.sendall(data.encode("utf-8"))
    
    def receive(self):
        return self.sock.recv(1024).decode("utf-8")


client = Client()
for i in range(10):
    client.send(f"CLIENT {i+10}")
    resp = client.receive()
    if resp:
        print(resp)
    
    time.sleep(1)
