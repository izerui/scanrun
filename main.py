# -*- coding: UTF-8 -*-
import logging
import platform

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget
from shiboken6 import *

from controller.home import HomeWindow
from controller.login import LoginWindow
from utils.context import Context


# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    # 槽函数：显示登录页
    @Slot()
    def loadLoginWindow(self):
        self.login = LoginWindow()
        self.login.loginSuccessSignal.connect(self.loadHomeWindow)
        self.login.show()

    # 槽函数：显示登录后的主页
    @Slot()
    def loadHomeWindow(self):
        self.home = HomeWindow()
        self.home.loginExistSignal.connect(self.loadLoginWindow)
        self.home.show()

    def init(self):
        Context.setDefaultSettings('gateway/domain', 'https://yj2025.com')
        Context.setDefaultSettings('scan/auto_code', False)
        Context.setDefaultSettings('login/username', '')
        Context.setDefaultSettings('login/password', '')

        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        isDebug = True if sys.gettrace() else False
        if isDebug:
            logging.basicConfig(format=LOG_FORMAT)
        else:
            system = platform.system()
            if system == 'Windows':
                logging.basicConfig(filename=f'error.log', level=logging.ERROR,
                                    format=LOG_FORMAT)
            else:
                logging.basicConfig(filename=f'{os.environ["HOME"]}{os.sep}scanrun-error.log', level=logging.ERROR,
                                    format=LOG_FORMAT)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.loadLoginWindow()
    # app.setStyle(QStyleFactory.create('macOS'))
    sys.exit(app.exec())
