from typing import Callable

from PySide6.QtCore import QThread


class ThreadExecutor(object):
    def __init__(self):
        super().__init__()

    def execute_new_thread(self, thread_name: str, new_thread: QThread, signal_name: str = None,
                           connect_fun: Callable = None):
        if hasattr(self, thread_name) and getattr(self, thread_name).isRunning():
            pass
        else:
            setattr(self, thread_name, new_thread)
            if signal_name:
                getattr(getattr(self, thread_name), signal_name).connect(connect_fun)
            getattr(self, thread_name).start()
