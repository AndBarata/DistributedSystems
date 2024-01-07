import socket
import threading


class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.soc = socket.socket()
        self.soc.bind((self.host, self.port))
        self.soc.listen()

    def sendMessage(self, clientSocket, message):
        clientSocket.send(message.encode("utf-8"))

    def handleClient(self, clientSocket, clientAddress):
        while True:
            data = clientSocket.recv(1024).decode("utf-8")
            if data:
                print(data) # Display request
                self.sendMessage(clientSocket, f"SERVER | ACK {data}") # Send response
            else:
                break

    def start(self):
        print("Server started. Waiting for connection..")
        while True:
            conn, addr = self.soc.accept()
            print(f"Connected with {addr}")
            threading.Thread(target = self.handleClient, args=(conn, addr)).start()




server = Server()
server.start()