from common.state import *
class Task():
    """任务封装类，任务就是类的一个个实例"""
    def __init__(self, id, script, timeout,  targets , paralell=1, fail_count=0, fail_rate=0):
        self.id = id
        self.script = script
        self.timeout = timeout

        self.targets = targets
        self.state = WAITING
        self.paralell = paralell
        self.fail_count = fail_count
        self.fail_rate = fail_rate
    def __repr__(self):
        return '<Task {}>'.format(self.id)


