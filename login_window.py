# -*- coding: UTF-8 -*-
import json

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox, QWidget

from net_request import FkRequest
from ui.ui_login import Ui_Login_Form


class LoginWindow(QWidget):
    loginSuccessSignal = Signal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login_Form()
        self.ui.setupUi(self)
        self.changeButtonState()

    # 改变提交按钮状态
    def changeButtonState(self):
        if len(self.ui.usernameInput.text()) > 0 and len(self.ui.passwordInput.text()) > 0:
            self.ui.subButton.setEnabled(True)
        else:
            self.ui.subButton.setDisabled(True)

    def loginForm(self):
        postJson = {
            'username': self.ui.usernameInput.text(),
            'password': self.ui.passwordInput.text(),
            'type': 1
        }
        # try:
        res = FkRequest.post('https://yj2025.com/ierp/login', postJson)
        if res.status_code == 200 and json.loads(res.text)['success']:
            FkRequest.setCookies(res.headers.get('set-cookie'))
            self.loginSuccessSignal.emit('loginSuccess')
            self.close()
        else:
            QMessageBox.critical(None, '错误', '登录验证失败')
        # except:
        #     QMessageBox.information(self, '异常', '登录碰到异常')

    def resetForm(self):
        self.ui.usernameInput.setText('')
        self.ui.passwordInput.setText('')
        self.ui.subButton.setEnabled(False)
        self.ui.usernameInput.setFocus()