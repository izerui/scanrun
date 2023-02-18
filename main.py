# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget, QStyleFactory

from home import HomeWindow
from login import LoginWindow

class MainWindow(QWidget):


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.loadLoginWindow()
    # app.setStyle(QStyleFactory.create('macOS'))
    sys.exit(app.exec())
