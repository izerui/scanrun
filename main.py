# -*- coding: UTF-8 -*-

# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QWidget

from controller.home import HomeWindow
from controller.login import LoginWindow
from utils.context import Context


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initDefaultSettings()

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

    def initDefaultSettings(self):
        Context.setDefaultSettings('gateway/domain', 'https://yj2025.com')
        Context.setDefaultSettings('scan/auto_code', False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.loadLoginWindow()
    # app.setStyle(QStyleFactory.create('macOS'))
    sys.exit(app.exec_())