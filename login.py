# -*- coding: UTF-8 -*-
import json
import sys

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QMessageBox, QWidget

from executor import ThreadExecutor
from request import PostThread, Request
from ui.ui_login import Ui_Login_Form


class LoginWindow(QWidget, Ui_Login_Form, ThreadExecutor):
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
        self.execute_new_thread('loginThread',
                                PostThread('https://yj2025.com/ierp/login', data),
                                'resultSignal',
                                self.loginSuccess)
        pass

    def loginSuccess(self, result):
        if result.status_code == 200 and json.loads(result.text)['success']:
            Request.setCookies(result.headers.get('set-cookie'))
            self.loginSuccessSignal.emit('success')
            self.close()
        else:
            self.process_label.setVisible(False)
            QMessageBox.critical(None, '错误', '登录验证失败')
        pass

    @Slot()
    def existForm(self):
        sys.exit()
        pass
