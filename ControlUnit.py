import socket
import time

class ControlUnit:
    def __init__(self, ip):
        self.ip = ip
        self.PM_Port = 1027
        self.HTP_Port = 1025
        self.MESSAGE = b"a"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(False)

    def change_ip(self, ip):
        self.ip = ip

    def get_pm(self):
        try:
            self.sock.sendto(b"a", (self.ip, self.PM_Port))
            time.sleep(0.1)
            rawdata = self.sock.recvfrom(1024)
            data = rawdata[0].decode("utf-8")
            #print(rawdata[1][1], end = " ")
            if rawdata[1][1] == self.PM_Port:
                pm2p5 = data.split(";")[0]
                pm10 = data.split(";")[1]
            else:
                pm2p5 = -1
                pm10 = -1
        except:
            pm2p5 = -1
            pm10 = -1
        return pm2p5, pm10

    def get_htp(self):
        try:
            self.sock.sendto(b"a", (self.ip, self.HTP_Port))
            time.sleep(0.1)
            rawdata = self.sock.recvfrom(1024)
            #print(rawdata[1][1], end=" ")
            data = rawdata[0].decode("utf-8")
            if rawdata[1][1] == self.HTP_Port:
                T = data.split(";")[0]
                H = data.split(";")[1]
                P = data.split(";")[2]
            else:
                w=self.sock.recvfrom(1024)
                T = -1
                H = -1
                P = -1
        except:
            T = -1
            H = -1
            P = -1
        return T,H,P

if __name__ == "__main__":
    cu = ControlUnit("192.168.1.5")
    while True:
        #cu.get_pm()
        print(cu.get_pm())
        print(cu.get_htp())
        time.sleep(1)

 
