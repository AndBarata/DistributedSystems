import socket
import threading

class Server():
    def __init__(self):
        self.host = "localhost"
        self.port = 33001
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()


    def receive(self, conn):
        return conn.recv(1024).decode("utf-8")

    def send(self, data, conn):
        conn.sendall(data.encode("utf-8"))

    def start(self):
        while True:
            conn, addr = self.sock.accept()
            print(f"New connection with {addr}")
            threading.Thread(target = self.handleConnection, args = (conn, addr)).start()

    def handleConnection(self, conn, addr):
        while True:
            data = self.receive(conn)
            if data:
                self.send(f"ACK  {addr} - {data}", conn)
                print(data)



server = Server()
server.start()


        