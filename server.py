import socket
import datetime


class Server:
    def __init__(self):
        self.port = 123
        self.address = "127.0.0.1"
        self.offset = self.read_offset()

    def get_time_with_offset(self):
        time = datetime.datetime.now()
        return time + datetime.timedelta(seconds=self.offset)

    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as so:
            so.bind((self.address, self.port))
            while True:
                data, sender = so.recvfrom(254)
                so.sendto(str(self.get_time_with_offset()).encode("utf-8"), sender)

    @staticmethod
    def read_offset():
        with open("conf.txt", "r") as f:
            line = f.readline()
            return int(line)


s = Server()
s.listen()
