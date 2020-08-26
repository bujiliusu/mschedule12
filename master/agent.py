import datetime
from common.state import *
class Agent():
    """客户端注册后的信息要封装，提供一个信息存储的类，数据存储在实例中"""
    def __init__(self, id, hostname, ip):
        self.regtime = datetime.datetime.now()
        self.id = id
        self.hostname = hostname
        self.ip = ip
        self.state = WAITING
        self.outputs = {}
    def __repr__(self):
        return '<Agent {} {} {}'.format(self.id, self.hostname, self.ip)
