import socket
import struct
import time
from datetime import datetime, timedelta
import threading

counter = 0 # DEBUG

class NTPclient():
    def __init__(self, update_rate):
        # Connection parameters
        self.host = "pool.ntp.org" # case of NTP online server
        #self.host = "10.42.0.1" # case of rasp
        self.port = 123
        self.read_buffer = 1024
        self.address = (self.host, self.port)
        self.epoch = 2208988800
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Fetch parameters
        self.update_rate = update_rate # seconds
        self.fetch_time = threading.Event()

    def start(self):
        while not self.fetch_time.wait(self.update_rate):
            global counter # DEBUG
            counter = 0 # DEBUG
            t = self.getServerTime()
            print("\nNTPserver time: ", t)

    def getServerTime(self):
        data = b'\x1b' + 47 * b'\0'
        self.client.sendto(data, self.address)

        data, self.address = self.client.recvfrom(self.read_buffer)

        t_int, t_frac = struct.unpack("!12I", data)[10:12]
        t_int -= self.epoch

        # Convert the fractional part to microseconds (1 second = 2**32 fractional units)
        t_frac = t_frac * 1e6 // 2**32

        # Format the NTP time as a string
        ntp_time = "%s.%06d" % (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(t_int)), t_frac)

        return ntp_time


class AbstractClock():
    # Is a clock that runs over the OS clock. It's updated according the the OS monotonic clock
    def __init__(self, update_rate):
        self.timestamp = 0
        self.update_rate = update_rate # seconds
        self.update_timer = threading.Event()

    def start(self):
        self.start_time = time.monotonic()
        self.start_datetime = datetime.now()
        while not self.update_timer.wait(self.update_rate):
            global counter # DEBUG
            counter += 1 # DEBUG
            self.updateTimestamp()
            print(f"[{counter}] Slave timestamp: {self.timestamp}")

    def updateTimestamp(self):
        self.timestamp = timedelta(seconds=(time.monotonic() - self.start_time))+ self.start_datetime
        
        
def monotomicSleep(seconds):
    # Sleep function that uses the monotonic clock
    start_time = time.monotonic()
    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time
        if elapsed_time >= seconds:
            break

if __name__ == "__main__":

    # Define update rates
    ABSTRACT_CLOCK_UPDATE_RATE = 0.1 # seconds
    NTP_UPDATE_RATE = 10 * ABSTRACT_CLOCK_UPDATE_RATE # seconds

    # Creates instances for clock and NTP client
    slave_clock = AbstractClock(ABSTRACT_CLOCK_UPDATE_RATE)
    ntp_client = NTPclient(NTP_UPDATE_RATE)

    # Start threads
    threading.Thread(target=slave_clock.start).start()
    monotomicSleep(ABSTRACT_CLOCK_UPDATE_RATE/5) # Sleep avoid overlapping between the two threads
    threading.Thread(target=ntp_client.start).start()



