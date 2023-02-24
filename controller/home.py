# -*- coding: UTF-8 -*-
import time

from PySide6.QtCore import Signal, Slot, QDateTime
from PySide6.QtWidgets import QMainWindow, QMessageBox, QStatusBar, QLabel
from apscheduler.schedulers.background import BackgroundScheduler

from ui.ui_home import Ui_Home
from utils.context import Context
from utils.executor import HttpExecutor, GetThread


####################
## 继承 QMainWindow、Ui_Home、ThreadExecutor
####################
class HomeWindow(QMainWindow, Ui_Home, HttpExecutor):
    # 登出信号
    loginExistSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 开始扫描信号
        self.taskFrame.scanConfirmedSignal.connect(self.scanConfirmed)
        self.scanFrame.returnHome.connect(self.returnHome)

        # style
        self.switchTab(0)

        self.loopGetUserInfo()
        schedule = BackgroundScheduler()
        schedule.add_job(self.loopGetUserInfo, trigger='interval', minutes=10)
        schedule.start()



    # 进入扫码页面
    @Slot()
    def scanConfirmed(self, scan_info: dict):
        if not Context.user:
            QMessageBox.critical(None, '提示', '未获取到登录用户信息')
        else:
            self.stackedTab.setCurrentIndex(2)
            self.leftFrame.setVisible(False)
            self.scanFrame.setScanInfo(scan_info)
            self.scanFrame.loadScanData()

    # @Slot()
    # def toolbarClicked(self, *args: QAction):
    #     if args[0].text() == 'home':
    #         self.switchTabPage(0)
    #     if args[0].text() == 'scan':
    #         self.openTaskForm()
    #     if args[0].text() == 'logout':
    #         self.logout()
    # QMessageBox.information(None, '提示', '深圳云集智造系统有限公司')

    @Slot()
    def logout(self):
        self.loginExistSignal.emit('logout')
        self.close()

    @Slot()
    def tabButtonPressed(self):
        checkedButtonText = self.tabButtonGroup.checkedButton().objectName()
        if checkedButtonText == 'btn_task':
            self.switchTab(0)
        elif checkedButtonText == 'btn_data':
            self.switchTab(1)

    def switchTab(self, index):
        self.stackedTab.setCurrentIndex(index)
        self.leftFrame.setVisible(True)
        if index > 1:
            self.leftFrame.setVisible(False)

    def returnHome(self):
        self.switchTab(0)

    # 每10分钟获取一次用户信息，保持session在线
    def loopGetUserInfo(self):
        self.execute(
            'loopGetUserInfoThread',
            GetThread(f'{Context.getSettings("gateway/domain")}/ierp/v2/user/info/1', postCode='M1200'),
            self.userInfoResponse
        )

    def userInfoResponse(self, result):
        Context.user = result['data']