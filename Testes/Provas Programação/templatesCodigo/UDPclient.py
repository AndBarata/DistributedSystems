import socket
import time

class Client():
    def __init__(self):
        self.host = "localhost"
        self.port = 3334
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(5)

    def send(self, data, addr):
        self.sock.sendto(data.encode("utf-8"), (self.host, self.port))

    def receive(self):
        try: 
            data, addr = self.sock.recvfrom(1024)
        except socket.timeout:
            print("Request timeout")
            return None

        return data.decode("utf-8"), addr




client = Client()
for i in range(10):
    client.send(f"CLIENT: {i}", (client.host, client.port))
    data, addr = client.receive()
    if data:
        print(data)
    time.sleep(1)
