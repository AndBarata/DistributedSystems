class NTPclient():
    def __init__(self, update_rate):
        # Connection parameters
        self.host = "pool.ntp.org" # case of NTP online server
        #self.host = "10.42.0.1" # case of rasp
        #self.host = "192.168.0.0"
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
