import socket
import threading
import sys

class Server():
    def __init__(self, port, average):
        self.average = float(average)

        self.host = "localhost"
        self.port = int(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM for TCP
        self.sock.bind((self.host, self.port))
        self.sock.listen()

    def send(self, data, conn):
        conn.sendall(data.encode("utf-8"))


    def receive(self, conn):
        return conn.recv(1024).decode("utf-8")

    def handleConnection(self, conn, addr):
        while True:
            request = self.receive(conn)
            if request:
                print(f"RX_SERVER | {request}")
                self.send(f"{self.average}", conn)
                print(f"TX_SERVER | {self.average}")


    def start(self):
        while True:
            conn, addr = self.sock.accept()
            print(f"New connection with: {addr}")
            threading.Thread(target = self.handleConnection, args = (conn, addr)).start()


if len(sys.argv) != 3:
    print("Error in arguments. python3 Server.py <port> <average>")
    sys.exit()

print(f"DEBUG len arg: {sys.argv[1]}")


server = Server(sys.argv[1], sys.argv[2])
server.start()
