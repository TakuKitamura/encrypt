import datetime
from time import ctime
import sys
import ntplib

class NTPClient(object):
    def __init__(self, ntp_server_host):
        self.ntp_client = ntplib.NTPClient()
        self.ntp_server_host = ntp_server_host

    def get_nowtime(self):
        try:
            res = self.ntp_client.request(self.ntp_server_host)
            utc = datetime.datetime.utcfromtimestamp(res.tx_time)
            return utc
        except Exception as e:
            print("An error occured")
            print("The information of error is as following")
            print(type(e))
            print(e.args)
            print(e)
            exit(1)

# def main():
#     ntp_client = NTPClient('0.europe.pool.ntp.org')
#     print(ntp_client.get_nowtime())

# if __name__ == "__main__":
#     main()