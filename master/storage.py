from .agent import Agent
from .task import Task
import uuid
from common.state import *
class Storage:
    """存储agent,task"""
    def __init__(self):
        self.agents = {}
        self.tasks = {}
    def reg(self, id, hostname, ip):
        if id not in self.agents.keys():
            self.agents[id] = Agent(id, hostname, ip)
        else:
            agent = self.agents[id]
            agent.hostname = hostname
            agent.ip = ip
    def heartbeat(self, id, hostname, ip):
        if id not in self.agents.keys():
            self.agents[id] = Agent(id, hostname, ip)
        else:
            agent = self.agents[id]
            agent.hostname = hostname
            agent.ip = ip
    def add_task(self, task:dict):
        id = uuid.uuid4().hex
        t = Task(id, **task)
        t.targets = { agent_id:self.agents[agent_id] for agent_id in t.targets }
        self.tasks[t.id] = t
        return t.id
    def iter_task(self, states={WAITING, RUNNING}):
        # for task in self.tasks.values():
        #     if task.state in states:
        #         yield task
        yield from (task for task in self.tasks.values() if task.state in states)
    def get_task(self, agent_id):
        for task in self.iter_task():
            if agent_id in task.targets.keys():
                agent = self.agents[agent_id]
                if task.id not in agent.outputs.keys():
                    agent.outputs[task.id] = None
                    task.state = RUNNING
                    agent.state = RUNNING
                    return (task.id, task.script, task.timeout)
    def result(self, msg):
        agent_id = msg['id']
        agent = self.agents[agent_id]
        agent.outputs[msg['task_id']] = {
            'code': msg['code'],
            'output': msg['output']
        }
    def get_agents(self):
        return {agent.id:agent.hostname for agent in self.agents.values()}


