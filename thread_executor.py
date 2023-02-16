
class ThreadExecutor(object):
    def __init__(self):
        super().__init__()

    def execute_new_thread(self, threadName, newThread, signalName=None, connectFun=None):
        if hasattr(self, threadName) and self[threadName].isRunning():
            pass
        else:
            setattr(self, threadName, newThread)
            if not signalName:
                self[threadName][signalName].connect(connectFun)
            self[threadName].start()
