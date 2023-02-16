# -*- coding: UTF-8 -*-
import json

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox, QWidget

from request import PostThread, Request
from thread_executor import ThreadExecutor
from ui.ui_login import Ui_Login_Form


class LoginWindow(QWidget, ThreadExecutor):
    loginSuccessSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Login_Form()
        self.ui.setupUi(self)
        self.ui.process_label.setVisible(False)
        self.changeButtonState()

    # 改变提交按钮状态
    def changeButtonState(self):
        if len(self.ui.usernameInput.text()) > 0 and len(self.ui.passwordInput.text()) > 0:
            self.ui.subButton.setEnabled(True)
        else:
            self.ui.subButton.setDisabled(True)

    def loginForm(self):
        self.ui.subButton.setDisabled(True)
        self.ui.process_label.setVisible(True)
        data = {
            'username': self.ui.usernameInput.text(),
            'password': self.ui.passwordInput.text(),
            'type': 1
        }
        self.execute_new_thread('loginThread',
                                PostThread('https://yj2025.com/ierp/login', data),
                                'resultSignal',
                                self.loginSuccess)

    def loginSuccess(self, result):
        if result.status_code == 200 and json.loads(result.text)['success']:
            Request.setCookies(result.headers.get('set-cookie'))
            self.loginSuccessSignal.emit('success')
            self.close()
        else:
            self.ui.process_label.setVisible(False)
            QMessageBox.critical(None, '错误', '登录验证失败')

    def resetForm(self):
        self.ui.usernameInput.setText('')
        self.ui.passwordInput.setText('')
        self.ui.subButton.setEnabled(False)
        self.ui.usernameInput.setFocus()
