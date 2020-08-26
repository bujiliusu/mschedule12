from .cm import ConnectionManager

class Master:
    def __init__(self):
        self.cm = ConnectionManager()
    def start(self):
        self.cm.start()
    def shutdown(self):
        self.cm.shutdown()
