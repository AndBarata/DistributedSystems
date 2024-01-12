import socket
import time
import threading

class Server:
    def __init__(self, host='0.0.0.0', port=12345):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(2)

    def handle_client(self, client_socket):
        filename = "data/V3/slots_corrected_delay_2NTP.txt"
        with open(filename, "a") as file:
            while True:
                data = client_socket.recv(1024)
                if data:
                    print(f"INFO : {data.decode('utf-8')}   \t@ {time.monotonic()}")
                    file.write(f"INFO : {data.decode('utf-8')}   \t@ {time.monotonic()}\n")
                    file.flush()  # Ensure immediate write to the file
                else:
                    break
        client_socket.close()

    def start(self):
        print("Monitor started, waiting for connections...")
        while True:
            client_socket, addr = self.sock.accept()
            print(f"Connection established with {addr} at date {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

# Usage
server = Server()
server.start()
