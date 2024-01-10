import socket

class Server():
    def __init__(self):
        self.host = "localhost"
        self.port = 3334
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", self.port))
        

    def send(self, data, addr):
        self.sock.sendto(data.encode("utf-8"), addr)

    def receive(self):
        data, addr = self.sock.recvfrom(1024)
        if data:
            return data.decode("utf-8"), addr
        else:
            return None


server = Server()
while True:
    data, addr = server.receive()
    if data:
        print(data)
        server.send(f"ACK | {data}", addr)


