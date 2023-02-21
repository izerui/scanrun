# -*- coding: UTF-8 -*-

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QMainWindow
from apscheduler.schedulers.background import BackgroundScheduler

from utils.executor import HttpExecutor, GetThread
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
        self.scanFrame.returnHome.connect(self.returnHome)

        # style
        self.switchTab(0)

        # self.loopGetUserInfo()
        schedule = BackgroundScheduler()
        schedule.add_job(self.loopGetUserInfo, trigger='interval', seconds=5)
        schedule.start()

    # 进入扫码页面
    def selectItemAndStart(self, dict):
        self.stackedTab.setCurrentIndex(2)
        self.leftFrame.setVisible(False)
        self.scanFrame.loadData()

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
            GetThread('https://yj2025.com/ierp/v2/user/info/1', postCode='M1200')
        )
