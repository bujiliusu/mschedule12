from utils import getlogger
from .agent import Agent
from .storage import Storage

logger = getlogger('__name__', 'd:/test/master.msg.log')

class Message:
    def __init__(self):
        self.storage = Storage()
    def reg(self, msg:dict):
        ts = msg['timestamp']
        logger.info(msg)
        self.storage.reg(msg['id'], msg['hostname'], msg['ip'])
        return 'reg {}'.format(msg)
    def heartbeat(self, msg):
        ts = msg['timestamp']
        logger.info(msg)
        self.storage.heartbeat(msg['id'], msg['hostname'], msg['ip'])
        return 'hb {}'.format(msg)
    def add_task(self, task:dict):
        id = self.storage.add_task(task)
        return id
    def pull_task(self, agent_id):

        return self.storage.get_task(agent_id)
    def result(self, msg):
        self.storage.result(msg)
        return 'ack result'
    def agents(self):
        return self.storage.get_agents()