from typing import Callable

from PySide6.QtCore import QThread


class ThreadExecutor(object):
    def __init__(self):
        super().__init__()

    def execute_new_thread(self, threadName:str, newThread:QThread, signalName:str=None, connectFun:Callable=None):
        if hasattr(self, threadName) and getattr(self, threadName).isRunning():
            pass
        else:
            setattr(self, threadName, newThread)
            if signalName:
                getattr(getattr(self, threadName), signalName).connect(connectFun)
            getattr(self, threadName).start()
