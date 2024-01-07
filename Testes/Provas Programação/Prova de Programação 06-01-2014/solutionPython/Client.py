import socket
import time

class Client():
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def sendData(self, data):
        self.soc.sendall(data.encode('utf-8'))

    def readData(self):
        return self.soc.recv(1024).decode('utf-8')
    def openConnection(self):
        self.soc.connect((self.host, self.port))

    def closeConnection(self):
        self.soc.close()


client = Client()
client.openConnection()
time.sleep(5)

for i in range(5):
    client.sendData(f"CLIENT | {i}")
    print(f"LOCAL | {i}")
    resp = client.readData()
    print(resp)
    time.sleep(2)