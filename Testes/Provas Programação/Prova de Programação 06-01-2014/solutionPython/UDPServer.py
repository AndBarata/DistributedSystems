import socket
import threading
import sys 

class Server():
    def __init__(self, port, average):
        self.average = float(average)

        self.host = "localhost"
        self.port = int(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host,self.port))

    def send(self, data, addr):
        self.sock.sendto(data.encode("utf-8"), addr)


    def receive(self):
        data, addr = self.sock.recvfrom(1024)
        return data.decode("utf-8"), addr

if len(sys.argv) != 3:
    print("Error in arguments. python3 Server.py <port> <average>")
    sys.exit()


server = Server(sys.argv[1], sys.argv[2])

while True:
    request, addr = server.receive()
    if request:
        print(f"RX_SERVER | {request}")
        server.send(f"{server.average}", addr)
        print(f"TX_SERVER | {server.average}")
