# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys

from PySide6.QtWidgets import QApplication, QWidget

from home_window import HomeWindow
from login_window import LoginWindow

class MainWindow(QWidget):


    # 显示登录页
    def loadLoginWindow(self):
        self.login = LoginWindow()
        self.login.loginSuccessSignal.connect(self.loadHomeWindow)
        self.login.show()

    # 显示登录后的主页
    def loadHomeWindow(self):
        self.home = HomeWindow()
        self.home.loginExistSignal.connect(self.loadLoginWindow)
        self.home.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.loadLoginWindow()
    sys.exit(app.exec())
