from .config import *
import zerorpc
from .message import Message

class ConnectionManager:
    def __init__(self):
        self.server = zerorpc.Server(Message())
        self.server.bind(MASTER_URL)
    def start(self):
        self.server.run()
    def shutdown(self):
        self.server.close()