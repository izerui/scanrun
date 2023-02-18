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
    loginExistSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initStyle()
        self.loadOrders()

    def toolbarClicked(self):
        QMessageBox.information(None, '提示', '深圳云集智造系统有限公司')

    def loadOrders(self):
        self.tableWidget.setRowCount(0)
        reqParam = {"docStatus": "DRAFT", "pageIndex": 0, "pageSize": 20, "total": 0}
        self.execute_new_thread('loadDataThread',
                                PostThread('https://yj2025.com/ierp/sale-pc/v1/sale/order/list', json=reqParam,
                                           postCode='M1018'),
                                'resultSignal',
                                self.dataResponse
                                )

    def dataResponse(self, result):
        data = json.loads(result.text)['data']
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
        pass
