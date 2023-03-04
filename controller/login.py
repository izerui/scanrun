# -*- coding: UTF-8 -*-
import sys

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QMessageBox

from ui.ui_login import Ui_Login_Form
from utils.context import Context
from utils.executor import HttpExecutor, PostThread
from utils.request import Request


class LoginWindow(QWidget, Ui_Login_Form, HttpExecutor):
    loginSuccessSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.process_label.setVisible(False)
        self.readDefaultText()
        self.changeButtonState()

    def readDefaultText(self):
        username = Context.getSettings('login/username')
        if username:
            self.usernameInput.setText(username)
        password = Context.getSettings('login/password')
        if password:
            self.passwordInput.setText(password)


    # 改变提交按钮状态
    def changeButtonState(self):
        self.process_label.setVisible(False)
        if len(self.usernameInput.text()) > 0 and len(self.passwordInput.text()) > 0:
            self.subButton.setEnabled(True)
        else:
            self.subButton.setDisabled(True)

    @Slot()
    def loginForm(self):
        self.subButton.setDisabled(True)
        self.process_label.setVisible(True)
        data = {
            'username': self.usernameInput.text(),
            'password': self.passwordInput.text(),
            'type': 1
        }
        self.http(
            'loginThread',
            PostThread(f'{Context.getSettings("gateway/domain")}/ierp/login', data),
            self.loginSuccess,
            lambda err: (
                QMessageBox.critical(None, '错误', err['errMsg']),
                self.process_label.setVisible(False)
            )
        )

    def loginSuccess(self, result, response):
        self.process_label.setVisible(False)
        Request.setCookies(response.headers.get('set-cookie'))
        self.loginSuccessSignal.emit('success')
        self.close()

    @Slot()
    def existForm(self):
        sys.exit()
