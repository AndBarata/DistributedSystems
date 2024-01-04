import socket
import struct
import time
from datetime import datetime, timedelta
import threading
import ntplib
import sys

counter = 0 # DEBUG



class NTPclient():
    def __init__(self, update_rate, slave_clock):
        self.slave_clock = slave_clock
        self.client = ntplib.NTPClient()
        self.server = '0.pool.ntp.org'
        # Fetch parameters
        self.update_rate = update_rate # seconds
        self.fetch_time = threading.Event()
        self.lastResponse = 0

    def start(self):
        while not self.fetch_time.wait(self.update_rate):
            global counter # DEBUG
            counter = 0 # DEBUG
            self.slave_clock.sentRequestTime = self.slave_clock.timestamp
            resp = self.getServerTime()
            self.slave_clock.calculateOffset(resp)


    def getServerTime(self):
        try:
            resp = self.client.request(self.server, version=3)
            self.lastResponse = resp
        except:
            resp = self.lastResponse
        return resp
        



class AbstractClock():
    # Is a clock that runs over the OS clock. It's updated according the the OS monotonic clock
    def __init__(self, update_rate, drift):
        self.timestamp = datetime.now()
        self.update_rate = update_rate # seconds
        self.drift = drift # seconds
        self.offset = timedelta(seconds=0)
        self.sentRequestTime = 0
        self.lastUpdate = 0
        self.update_timer = threading.Event()
    

    def start(self):
        self.start_time = time.monotonic()
        self.start_datetime = datetime.now()
        self.timestamp = datetime.now()
        while not self.update_timer.wait(self.update_rate):
            global counter # DEBUG
            counter += 1 # DEBUG
            self.updateTimestamp()
            print(f"[{counter}] Slave timestamp: {self.correctedTimestamp} | Offset: {self.offset}")



    def ntp_to_datetime(self, ntp_timestamp):
        ntp_epoch = datetime(1900, 1, 1)
        unix_epoch = datetime(1900, 1, 1)
        ntp_delta = (unix_epoch - ntp_epoch).total_seconds()

        timestamp = ntp_timestamp - ntp_delta
        return datetime.utcfromtimestamp(timestamp)    


    def calculateOffset(self, resp):

        # Calculate the offset between the slave and the master
        t3 = self.timestamp
        t2 = self.ntp_to_datetime(resp.tx_time)
        t1 = self.ntp_to_datetime(resp.recv_time)
        t0 = self.sentRequestTime
        
        print(f"\nNTP request: t3: {t3} | t2: {t2} | t1: {t1} | t0: {t0}") 
        self.offset = ( (t1-t0) + (t2-t3) ) / 2


    def updateTimestamp(self):
        # Update the timestamp according to the monotonic clock and the calculated offset
        #self.timestamp = timedelta(seconds=(time.monotonic() - self.start_time)) + self.start_datetime + timedelta(self.offset)
        
        self.timestamp = self.timestamp + timedelta(seconds=self.update_rate) + timedelta(seconds=self.drift)
        print("DEBUG: ", self.timestamp, "offset: ", self.offset)
        self.correctedTimestamp = self.timestamp + self.offset





def monotomicSleep(seconds):
    # Sleep function that uses the monotonic clock
    start_time = time.monotonic()
    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time
        if elapsed_time >= seconds:
            break


# Define update rates
ABSTRACT_CLOCK_UPDATE_RATE = 0.0001 # seconds 
NTP_UPDATE_RATE = 10 * ABSTRACT_CLOCK_UPDATE_RATE # seconds -> This can't be to low so that we have time to fetch the NTP time

# Adds a drift to the clock if specified, to see the results of the correction
if len(sys.argv) > 1:
    drift = float(sys.argv[1])
else:
    drift = 0 

# Creates instances for clock and NTP client
slave_clock = AbstractClock(ABSTRACT_CLOCK_UPDATE_RATE, drift)
ntp_client = NTPclient(NTP_UPDATE_RATE, slave_clock)

if __name__ == "__main__":

    # Start threads
    threading.Thread(target=slave_clock.start).start()
    monotomicSleep(ABSTRACT_CLOCK_UPDATE_RATE/5) # Sleep avoid overlapping between the two threads
    threading.Thread(target=ntp_client.start).start()








