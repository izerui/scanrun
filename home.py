# -*- coding: UTF-8 -*-

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
from apscheduler.schedulers.background import BackgroundScheduler

from dialog import TaskFormDialog
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
        self.initStyle()
        self.pageIndex = 0
        self.pageSize = 20
        self.totalPage = 0
        self.totalCount = 0
        self.homeAction.setVisible(False)
        # self.loopGetUserInfo()
        schedule = BackgroundScheduler()
        schedule.add_job(self.loopGetUserInfo, trigger='interval', seconds=5)
        schedule.start()
        self.firstPage()
        pass

    @Slot()
    def toolbarClicked(self, *args: QAction):
        if args[0].text() == 'home':
            self.returnHome()
        if args[0].text() == 'scan':
            self.openTaskForm()
        if args[0].text() == 'logout':
            self.logout()
        # QMessageBox.information(None, '提示', '深圳云集智造系统有限公司')
        pass

    def loadData(self):
        self.tableWidget.setRowCount(0)
        reqParam = {"docStatus": "DRAFT", "pageIndex": self.pageIndex, "pageSize": self.pageSize, "total": 0}
        self.execute_http('loadDataThread',
                          PostThread('https://yj2025.com/ierp/sale-pc/v1/sale/order/list', json=reqParam,
                                     postCode='M1018'),
                          self.dataResponse
                          )
        pass

    @Slot()
    def firstPage(self):
        self.pageIndex = 0
        self.loadData()
        pass

    @Slot()
    def prePage(self):
        if self.pageIndex > 0:
            self.pageIndex -= 1
            self.loadData()
        else:
            QMessageBox.warning(None, '提示', '已经是第一页')
        pass

    @Slot()
    def nextPage(self):
        if self.pageIndex + 1 < self.totalPage:
            self.pageIndex += 1
            self.loadData()
        else:
            QMessageBox.warning(None, '提示', '已经是最后一页')
        pass

    @Slot()
    def endPage(self):
        if self.totalPage - 1 > 0:
            self.pageIndex = self.totalPage - 1
        self.loadData()
        pass

    @Slot()
    def jumpPage(self):
        if self.pageInput.value() >= self.totalPage:
            self.pageIndex = self.totalPage - 1
        else:
            self.pageIndex = self.pageInput.value() - 1
        self.loadData()
        pass

    def dataResponse(self, result):
        data = result['data']
        self.wrapPageData(data)
        self.dataResChangeView(data)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(len(data['content']))
        i = 0
        for d in data['content']:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(d['orderDocNo']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(d['customer']['customerName']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(d['customerOrderDocNo']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(d['totalOrderAmount']))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(d['employeeName']))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(d['createTime']))
            i += 1
        # self.tableWidget.show()
        self.tableWidget.selectRow(0)
        pass

    @Slot()
    def logout(self):
        self.loginExistSignal.emit('logout')
        self.close()
        pass

    def initStyle(self):
        self.treeWidget.expandAll()
        self.tableWidget.setShowGrid(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        pass

    def wrapPageData(self, data):
        self.dataList = data['content']
        self.pageIndex = data['number']
        self.totalPage = data['totalPages']
        self.totalCount = data['totalElements']
        self.pageSize = data['size']
        pass

    def dataResChangeView(self, data):
        self.pageInput.setValue(data['number'] + 1)
        self.label.setText(f'页 共{self.totalPage}页  {self.totalCount}条记录')
        pass

    @Slot()
    def dataRowSelected(self):
        self.selRow = self.dataList[self.tableWidget.currentRow() - 1]
        self.LineEdit_1.setText(self.selRow['orderDocNo'])
        self.LineEdit_2.setText(self.selRow['customer']['customerName'])
        self.LineEdit_3.setText(self.selRow['customerOrderDocNo'])
        self.LineEdit_4.setText(self.selRow['totalOrderAmount'])
        self.LineEdit_5.setText(self.selRow['employeeName'])
        self.LineEdit_6.setText(self.selRow['tax']['taxContent'])
        pass

    def startScanJob(self, dict):
        print(dict)
        self.stackedWidget.setCurrentIndex(1)
        self.scanAction.setVisible(False)
        self.homeAction.setVisible(True)
        pass

    @Slot()
    def openTaskForm(self):
        if self.selRow:
            self.task = TaskFormDialog()
            self.task.formCreated.connect(self.startScanJob)
            self.task.show()
        else:
            QMessageBox.warning(None, '提示', '请选择一条任务开始扫码')
        pass

    def returnHome(self):
        self.stackedWidget.setCurrentIndex(0)
        self.scanAction.setVisible(True)
        self.homeAction.setVisible(False)
        pass

    # 每10分钟获取一次用户信息，保持session在线
    def loopGetUserInfo(self):
        self.execute_http(
            'loopGetUserInfoThread',
            GetThread('https://yj2025.com/ierp/v2/user/info/1', postCode='M1200')
        )
        pass
