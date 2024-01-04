import socket
import struct
import time
from datetime import datetime, timedelta
import threading
import ntplib
import sys

counter = 0 # DEBUG



class NTPclient():
    def __init__(self, start_monotonic, start_datetime):
        # Connection parameters
        self.host = '0.pool.ntp.org' # case of NTP online server
        self.port = 123
        self.read_buffer = 1024
        self.address = (self.host, self.port)
        self.epoch = 2208988800
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.start_monotonic = start_monotonic
        self.start_datetime = start_datetime

    def monotonicToDatetime(self, now, start = 0):
        variation = timedelta(seconds=(now-start))
        elapsed_datetime = self.start_datetime + variation

        return elapsed_datetime


    def getServerTime(self):

        '''
        This function communicates with an NTP server to get the server time. It sends a request to the server, 
        receives the response, unpacks the timestamps from the response, and converts these timestamps to datetime objects.

        The function returns five datetime objects:
        - ref_time: Reference since the NTP clock started (Jan. 1st, 1900)
        - orig_time: The local time when the request was sent
        - rx_time: The time at the NTP server when the response was received.
        - tx_time: The time at the NTP server when the response was sent.
        - dest_time: The local time when the response was received.
        '''

        data = b'\x1b' + 47 * b'\0'
        orig_time = time.monotonic()
        self.client.sendto(data, self.address)
        data, self.address = self.client.recvfrom(self.read_buffer)
        orig_int, orig_frac, ref_int, ref_frac, rx_int, rx_frac, tx_int, tx_frac = struct.unpack("!12I", data)[4:12]


        rx_int -= self.epoch
        tx_int -= self.epoch

        # Convert the fractional part to microseconds (1 second = 2**32 fractional units)
        ref_frac = ref_frac * 1e6 // 2**32
        rx_frac = rx_frac * 1e6 // 2**32
        tx_frac = tx_frac * 1e6 // 2**32
        
        
        t_timedelta = timedelta(microseconds=ref_frac)
        ref_time = datetime.fromtimestamp(ref_int) + t_timedelta

        t_timedelta = timedelta(microseconds=rx_frac)
        rx_time = datetime.fromtimestamp(rx_int) + t_timedelta

        t_timedelta = timedelta(microseconds=tx_frac)
        tx_time = datetime.fromtimestamp(tx_int) + t_timedelta

        orig_time = self.monotonicToDatetime(orig_time, self.start_monotonic)
        dest_time = self.monotonicToDatetime(time.monotonic(), self.start_monotonic)

        return ref_time, orig_time, rx_time, tx_time, dest_time 
        



class AbstractClock():
    def __init__(self):

        # Clock correction parameters
        self.delay = 0
        self.last_offset = 0
        self.offset = 0
        self.rate = 1
        self.last_rate = 1
        
        # Time parameters for rate
        self.start_datetime = datetime.now() # datetime of when the clock was started
        self.start_monotonic = time.monotonic() # monotonic time of when the clock was started

        # NTP client
        self.ntp_client = NTPclient(self.start_monotonic, self.start_datetime)
        self.ntp_timestamp = self.ntp_client.getServerTime()[2] # datetime of when the NTP server was polled
        self.last_ntp_timestamp = self.ntp_timestamp

        # intrinsic clock attributes
        self.timestamp = time.monotonic()
        self.last_timestamp = self.timestamp
        

    def correctClock(self):
        ntp_time = self.ntp_client.getServerTime()
        t0 = ntp_time[1]
        t1 = ntp_time[2]
        t2 = ntp_time[3]
        t3 = ntp_time[4]
        # Update the rate parameters
        self.last_ntp_timestamp = self.ntp_timestamp
        self.ntp_timestamp = t1
        self.last_timestamp = self.timestamp
        self.timestamp = time.monotonic()

        self.updateOffset(t0, t1, t2, t3)
        self.updateRate(t0, t1, t2, t3)
        self.updateDelay(t0, t1, t2, t3)
        


    def updateOffset(self, t0, t1, t2, t3):
        self.last_offset = self.offset
        self.offset = ( t1-t3 + t2-t0) / 2

    def updateRate(self, t0, t1, t2, t3):
        self.last_rate = self.rate
        self.rate = abs((self.timestamp - self.last_timestamp) / (self.ntp_timestamp - self.last_ntp_timestamp).total_seconds())

    def updateDelay(self, t0, t1, t2, t3):
        self.delay = (t3-t0) - (t2-t1)

    def getCorrectedTime(self):
        now = time.monotonic()
        elapsed_time = now - self.timestamp
        
        corrected_time = self.timestamp + elapsed_time*self.rate + self.offset.total_seconds()

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run_clock)
        self.thread.start()

    def run_clock(self):
        while self.running:
            self.correctClock()
            rate = self.rate
            offset = self.offset.total_seconds()
            ts = self.timestamp
            t = time.monotonic()
            t_corrected = ts + (t-ts)*rate + offset
            print(self.ntp_client.monotonicToDatetime(t_corrected, self.start_monotonic))
            time.sleep(1)  # sleep for a while before next update

    def stop(self):
        self.running = False
        self.thread.join()





def monotomicSleep(seconds):
    # Sleep function that uses the monotonic clock
    start_time = time.monotonic()
    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time
        if elapsed_time >= seconds:
            break


# Define update rates
NTP_UPDATE_RATE = 0.1 # seconds -> This can't be to low so that we have time to fetch the NTP time

# Adds a drift to the clock if specified, to see the results of the correction
if len(sys.argv) > 1:
    drift = float(sys.argv[1])
else:
    drift = 0 

# Creates instances for clock and NTP client
slave_clock = AbstractClock()
#ntp_client = NTPclient(NTP_UPDATE_RATE, slave_clock)

if __name__ == "__main__":

    # Start threads
    threading.Thread(target=slave_clock.start).start()
    #threading.Thread(target=ntp_client.start).start()