# -*- coding: UTF-8 -*-
import sys

from PySide6 import QtCore
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QMessageBox

from ui.ui_login import Ui_Login
from utils.context import Context
from utils.executor import HttpExecutor, PostThread
from utils.request import Request


class LoginWindow(QWidget, Ui_Login, HttpExecutor):
    loginSuccessSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.readDefaultText()
        self.setSubButtonDefault()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())

    def readDefaultText(self):
        username = Context.getSettings('login/username')
        if username:
            self.usernameInput.setText(username)
        password = Context.getSettings('login/password')
        if password:
            self.passwordInput.setText(password)

    # 改变提交按钮状态
    def changeButtonState(self):
        if len(self.usernameInput.text()) > 0 and len(self.passwordInput.text()) > 0:
            self.subButton.setEnabled(True)
        else:
            self.subButton.setDisabled(True)

    @Slot()
    def login(self):
        self.setSubButtonLoading()
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
                self.setSubButtonDefault()
            )
        )

    def loginSuccess(self, result, response):
        self.setSubButtonDefault()
        Request.setCookies(response.headers.get('set-cookie'))
        self.loginSuccessSignal.emit('success')
        self.close()

    def setSubButtonDefault(self):
        self.subButton.setText('登录')
        self.changeButtonState()

    def setSubButtonLoading(self):
        self.subButton.setText('登录中...')
        self.subButton.setEnabled(False)

    @Slot()
    def exist(self):
        sys.exit()
