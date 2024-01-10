import socket
import struct
import time

class TemperatureSensor:
    def __init__(self, readings, multicast_group='224.3.29.71', port=10000):
        self.readings = readings
        self.multicast_group = multicast_group
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ttl = struct.pack('b', 1)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, self.ttl)

    def start(self):
        for reading in self.readings:
            message = f'Temperature: {reading}'
            print(f'Sending: {message}')
            self.sock.sendto(message.encode('utf-8'), (self.multicast_group, self.port))
            time.sleep(1)

if __name__ == "__main__":
    readings = [22.5, 23.1, 22.8, 23.0, 22.9]
    sensor = TemperatureSensor(readings)
    sensor.start()