# -*- coding: UTF-8 -*-
import json

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView

from executor import ThreadExecutor
from request import PostThread
from ui.ui_home import Ui_Home


####################
## 继承 QMainWindow、Ui_Home、ThreadExecutor
####################
class HomeWindow(QMainWindow, Ui_Home, ThreadExecutor):
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
        self.firstPage()

    @Slot()
    def toolbarClicked(self):
        QMessageBox.information(None, '提示', '深圳云集智造系统有限公司')

    def loadData(self):
        self.tableWidget.setRowCount(0)
        reqParam = {"docStatus": "DRAFT", "pageIndex": self.pageIndex, "pageSize": self.pageSize, "total": 0}
        self.execute_new_thread('loadDataThread',
                                PostThread('https://yj2025.com/ierp/sale-pc/v1/sale/order/list', json=reqParam,
                                           postCode='M1018'),
                                'resultSignal',
                                self.dataResponse
                                )

    @Slot()
    def firstPage(self):
        self.pageIndex = 0
        self.loadData()

    @Slot()
    def prePage(self):
        if self.pageIndex > 0:
            self.pageIndex -= 1
            self.loadData()
        else:
            QMessageBox.warning(None, '提示', '已经是第一页')

    @Slot()
    def nextPage(self):
        # TODO 判断 总页数
        if self.pageIndex + 1 < self.totalPage:
            self.pageIndex += 1
            self.loadData()
        else:
            QMessageBox.warning(None, '提示', '已经是最后一页')

    @Slot()
    def endPage(self):
        if self.totalPage - 1 > 0:
            self.pageIndex = self.totalPage - 1
        self.loadData()

    @Slot()
    def jumpPage(self):
        if self.pageInput.value() >= self.totalPage:
            self.pageIndex = self.totalPage - 1
        else:
            self.pageIndex = self.pageInput.value() - 1
        self.loadData()

    def dataResponse(self, result):
        data = json.loads(result.text)['data']
        self.wrapPage(data)
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

    @Slot()
    def logout(self):
        self.loginExistSignal.emit('logout')
        self.close()

    def initStyle(self):
        self.treeWidget.expandAll()
        self.tableWidget.setShowGrid(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def wrapPage(self, data):
        self.pageIndex = data['number']
        self.totalPage = data['totalPages']
        self.totalCount = data['totalElements']
        self.pageSize = data['size']

    def dataResChangeView(self, data):
        self.pageInput.setValue(data['number'] + 1)
        self.label.setText(f'页 共{self.totalPage}页  {self.totalCount}条')