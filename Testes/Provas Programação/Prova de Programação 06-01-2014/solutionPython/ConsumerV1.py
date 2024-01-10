import socket
import struct

class TemperatureConsumer:
    def __init__(self, multicast_group='224.3.29.71', port=10000):
        self.multicast_group = multicast_group
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', self.port))
        group = socket.inet_aton(self.multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def start(self):
        while True:
            print('Waiting for temperature readings...')
            data, address = self.sock.recvfrom(1024)
            print(f'Received {data.decode("utf-8")} from {address}')

if __name__ == "__main__":
    consumer = TemperatureConsumer()
    consumer.start()