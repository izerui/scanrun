# -*- coding: UTF-8 -*-

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
from apscheduler.schedulers.background import BackgroundScheduler

from controller.dialog import TaskFormDialog
from executor import HttpExecutor, PostThread, GetThread
from ui.ui_home import Ui_Home


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
        self.taskFrame.selectItemAndStart.connect(self.selectItemAndStart)

        # style
        self.homeAction.setVisible(False)
        self.stackedTab.setCurrentIndex(0)

        # self.loopGetUserInfo()
        schedule = BackgroundScheduler()
        schedule.add_job(self.loopGetUserInfo, trigger='interval', seconds=5)
        schedule.start()

    def selectItemAndStart(self, dict):
        print(dict)
        self.stackedTab.setCurrentIndex(2)
        self.scanAction.setVisible(False)
        self.homeAction.setVisible(True)


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
            self.stackedTab.setCurrentIndex(0)
        elif checkedButtonText == 'btn_data':
            self.stackedTab.setCurrentIndex(1)

    def returnHome(self):
        self.scanAction.setVisible(True)
        self.homeAction.setVisible(False)

    # 每10分钟获取一次用户信息，保持session在线
    def loopGetUserInfo(self):
        self.execute_http(
            'loopGetUserInfoThread',
            GetThread('https://yj2025.com/ierp/v2/user/info/1', postCode='M1200')
        )
