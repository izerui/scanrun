# -*- coding: UTF-8 -*-
import sys

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from executor import HttpExecutor, PostThread, GetThread
from request import Request
from ui.ui_login import Ui_Login_Form


class LoginWindow(QWidget, Ui_Login_Form, HttpExecutor):
    loginSuccessSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.process_label.setVisible(False)
        self.changeButtonState()
        pass

    # 改变提交按钮状态
    def changeButtonState(self):
        if len(self.usernameInput.text()) > 0 and len(self.passwordInput.text()) > 0:
            self.subButton.setEnabled(True)
        else:
            self.subButton.setDisabled(True)
        pass

    @Slot()
    def loginForm(self):
        self.subButton.setDisabled(True)
        self.process_label.setVisible(True)
        data = {
            'username': self.usernameInput.text(),
            'password': self.passwordInput.text(),
            'type': 1
        }
        self.execute_http(
            'loginThread',
            PostThread('https://yj2025.com/ierp/login', data),
            self.loginSuccess
        )
        pass

    def loginSuccess(self, result, response):
        self.process_label.setVisible(False)
        Request.setCookies(response.headers.get('set-cookie'))
        self.loginSuccessSignal.emit('success')
        self.close()
        pass

    @Slot()
    def existForm(self):
        sys.exit()
        pass
