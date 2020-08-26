from .cm import ConnectionManager
from .config import *
from .msg import Message
import threading
class Agent:
    def __init__(self):
        self.message = Message(MYID_PATH)
        self.cm = ConnectionManager(MASTER_URL, self.message)
        self.event = threading.Event()
    def start(self):
        while not self.event.is_set():
            try:
                self.cm.start()
            except Exception as e:
                pass
            self.event.wait(3)
            print('reconnect to {}'.format(MASTER_URL))
    def shutdown(self):
        self.cm.shutdown()
