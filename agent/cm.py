import zerorpc
import threading
from .msg import Message
from utils import getlogger
from .executor import Exexutor
from threading import Thread
from common.state import *
logger = getlogger(__name__, 'd:/test/cm.log')

class ConnectionManager:
    def __init__(self, master_url, message:Message):
        self.master_url=master_url
        self.client=zerorpc.Client()
        self.message=message
        self.event=threading.Event()
        self.executor = Exexutor()
        self.state = WAITING
        self.__result = None
    def _exec(self, task):
        task_id, script, timeout = task

        code, text = self.executor.run(script, timeout)
        print(code , text)
        self.__result = task_id, code, text
        self.state = SUCCESSFUL if code == 0 else FAILED
    def start(self, interval=5):
        try:
            self.client.connect(self.master_url)
            ack = self.client.reg(self.message.reg())
            logger.info("{}".format(ack))
            while not self.event.wait(interval):
                ack = self.client.heartbeat(self.message.heartbeat())
                logger.info("{}".format(ack))
                if self.state == WAITING:
                    task = self.client.pull_task(self.message.id)
                    if task:
                        self.state = RUNNING
                        Thread(target=self._exec, args=(task,)).start()

                if self.state in {SUCCESSFUL, FAILED}:
                    ack = self.client.result(self.message.result(*self.__result))
                    logger.info('{}'.format(self.__result))
                    self.__result = None
                    self.state = WAITING
        except Exception as e:
            logger.error(e)
            raise e
    def shutdown(self):
        self.event.set()
        self.client.close()
    def join(self):
        self.event.wait()
