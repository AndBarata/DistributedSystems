import socket
import threading
import random
import time
import sys

class Bully:
    def __init__(self, id, delay):
        self.id = id
        self.delay = delay
        self.election_mode = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', 10000 + id))

    def start(self):
        timeout = random.uniform(0, self.id * self.delay)
        time.sleep(timeout)
        self.start_election()

    def start_election(self):
        self.election_mode = True
        print(f"Node {self.id} started an election.")
        # Send 'ELECTION' message to all other nodes...

    def handle_message(self, message, sender_id):
        if message == 'ELECTION':
            if sender_id < self.id and self.election_mode:
                self.election_mode = False
                print(f"Node {self.id} cancelled its election.")
            elif not self.election_mode:
                self.start_election()

# Usage example
id1 = int(sys.argv[1])
delay1 = int(sys.argv[2])
bully1 = Bully(id1, delay1)
bully1.start()

id2 = int(sys.argv[3])
delay2 = int(sys.argv[4])
bully2 = Bully(id2, delay2)
bully2.start()

# Add more nodes as needed...