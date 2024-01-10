import socket
import struct
import time
from datetime import datetime, timedelta
import threading
import sys
import RPi.GPIO as GPIO

offsets = [] # For results

#define GPIOs
ledPin_vermelho = 17
ledPin_verde = 18

GPIO.setmode(GPIO.BCM)  # BCM scheme
GPIO.setwarnings(False) #ignore messages in terminal


#leds as outputs
GPIO.setup(ledPin_vermelho,GPIO.OUT)
GPIO.setup(ledPin_verde,GPIO.OUT)


class NTPclient():
    def __init__(self, start_monotonic, start_datetime):
        # Connection parameters
        self.host = 'pool.ntp.org' # case of NTP online server
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
        self.client.settimeout(5)  # set a timeout of 5 seconds
        
        try:
            
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
        

        except (socket.error, socket.timeout):
            # If a socket error occurs, print an error message and try again
            return 0
        
        



class AbstractClock():
    def __init__(self, NTP_UPDATE_RATE, drift = 0):

        # Clock correction parameters
        self.delay = 0
        self.last_offset = 0
        self.offset = 0
        self.rate = 1
        self.last_rate = 1
        self.drift = drift
        
        # Time parameters for rate
        self.start_datetime = datetime.now() # datetime of when the clock was started
        self.start_monotonic = time.monotonic() # monotonic time of when the clock was started

        # NTP client
        self.ntp_client = NTPclient(self.start_monotonic, self.start_datetime)
        self.last_ntp_timestamp = self.ntp_client.getServerTime()[2]
        self.ntp_timestamp = self.ntp_client.getServerTime()[3] # datetime of when the NTP server was polled
        

        # intrinsic clock attributes
        self.timestamp = time.monotonic()
        self.last_timestamp = self.timestamp
        
        self.correctClock()

    def correctClock(self):
        ntp_time = self.ntp_client.getServerTime()
        if ntp_time:
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
        
        else:
            print("Error connecting to NTP server. Retrying...")

        #print("\n_NTP update_\n") # DEBUG
        
        
        
        print(f"offset:{self.offset.total_seconds():.5f}")
        print(f"rate:{self.rate}")
        print(f"delay:{self.delay}")
        print("\n")
    
    def periodicClockUpdate(self):
        while True:
            self.correctClock()
            time.sleep(NTP_UPDATE_RATE)


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
        return self.ntp_client.monotonicToDatetime(corrected_time, self.start_monotonic)


class Monitor():
    def __init__(self, host='172.20.10.4', port=12345):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send_data(self, data):
        self.sock.sendall(data.encode('utf-8'))

    def close_connection(self):
        self.sock.close()







if __name__ == "__main__":

    # Define update rates
    NTP_UPDATE_RATE = 5 # seconds -> This can't be to low so that we have time to fetch the NTP time

    # Adds a drift to the clock if specified, to see the results of the correction
    side = 1 if len(sys.argv) <= 1 else sys.argv[1]
    drift = 0 if len(sys.argv) <= 2 else float(sys.argv[2])

    # Creates instances for clock and NTP client
    clock_A = AbstractClock(NTP_UPDATE_RATE, drift)
    monitor = Monitor() 

    threading.Thread(target=clock_A.periodicClockUpdate).start()
    
    state = 0
    prev_state = 0

    while True:
        abs_time = clock_A.getCorrectedTime()
        state = ((int(clock_A.getCorrectedTime().strftime('%S')) // 10) % 2 == 0) ^ int(side)
        if state and not prev_state:
            GPIO.output(ledPin_verde, GPIO.HIGH)    #turn only green on
            GPIO.output(ledPin_vermelho, GPIO.LOW)
            print("\Green:", clock_A.getCorrectedTime(), "\nMonotime: ", time.monotonic())
            monitor.send_data(f"{side} | Green") 
                    
        #state = (int(clock_A.getCorrectedTime().strftime('%S')) // 10) % 2 == 1 and side
        if not state and prev_state:   
            GPIO.output(ledPin_verde, GPIO.LOW)     #turn only red on
            GPIO.output(ledPin_vermelho, GPIO.HIGH)        
            print("\Red:", clock_A.getCorrectedTime(), "\nMonotime: ", time.monotonic())
            monitor.send_data(f"{side} | Red") 

        prev_state = state

