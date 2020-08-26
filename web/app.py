from agent import Agent

agent = Agent()
try:
    agent.start()
except KeyboardInterrupt:
    agent.shutdown()