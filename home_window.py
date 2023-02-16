import json

from PySide6 import QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox, QTableWidgetItem

from net_request import FkRequest
from ui.ui_home import Ui_Home


class HomeWindow(QMainWindow):
    loginExistSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.loadOrders()

    def toolbarClicked(self):
        QMessageBox.information(None, '提示', '深圳云集智造系统有限公司')

    def loadOrders(self):
        reqParam = {"docStatus": "DRAFT", "pageIndex": 0, "pageSize": 20, "total": 0}
        res = FkRequest.post('https://yj2025.com/ierp/sale-pc/v1/sale/order/list', json=reqParam, postCode='M1015')
        data = json.loads(res.text)['data']
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setRowCount(len(data['content']))
        i = 0
        for d in data['content']:
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(d['orderDocNo']))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(d['customer']['customerName']))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(d['customerOrderDocNo']))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(d['totalOrderAmount']))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(d['employeeName']))
            self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(d['createTime']))
            i += 1
        # self.ui.tableWidget.show()

    def logout(self):
        self.loginExistSignal.emit('logout')
        self.close()