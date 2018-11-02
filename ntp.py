import datetime
from time import ctime
import sys
import ntplib

class NTPClient(object):
    def __init__(self, ntp_server_host):
        self.ntp_client = ntplib.NTPClient()
        self.ntp_server_host = ntp_server_host

    def getNowtime(self):
        try:
            res = self.ntp_client.request(self.ntp_server_host)
            utc = datetime.datetime.utcfromtimestamp(res.tx_time)
            return utc
        except Exception as e:
            print(e)
            exit(1)
