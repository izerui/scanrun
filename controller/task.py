from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget, QHeaderView, QMessageBox, QTableWidgetItem

from controller.dialog import TaskFormDialog
from executor import HttpExecutor, PostThread
from ui.ui_task_frame import Ui_TaskFrame


class TaskFrame(QWidget, Ui_TaskFrame, HttpExecutor):

    selectItemAndStart = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initStyle()
        self.pageIndex = 0
        self.pageSize = 20
        self.totalPage = 0
        self.totalCount = 0
        self.firstPage()

    def initStyle(self):
        self.tableWidget.setShowGrid(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def loadData(self):
        self.tableWidget.setRowCount(0)
        reqParam = {"docStatus": "DRAFT", "pageIndex": self.pageIndex, "pageSize": self.pageSize, "total": 0}
        self.execute_http('loadDataThread',
                          PostThread('https://yj2025.com/ierp/sale-pc/v1/sale/order/list', json=reqParam,
                                     postCode='M1018'),
                          self.dataResponse
                          )

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

    def wrapPageData(self, data):
        self.dataList = data['content']
        self.pageIndex = data['number']
        self.totalPage = data['totalPages']
        self.totalCount = data['totalElements']
        self.pageSize = data['size']

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
        if self.pageEdit.value() >= self.totalPage:
            self.pageIndex = self.totalPage - 1
        else:
            self.pageIndex = self.pageEdit.value() - 1
        self.loadData()

    @Slot()
    def openTaskForm(self):
        if self.selRow:
            self.task = TaskFormDialog()
            # 两个信号连接，直接触发到home
            self.task.formCreated.connect(self.selectItemAndStart)
            self.task.show()
        else:
            QMessageBox.warning(None, '提示', '请选择一条任务开始扫码')

    @Slot()
    def dataRowSelected(self):
        self.selRow = self.dataList[self.tableWidget.currentRow() - 1]
        self.LineEdit_7.setText(self.selRow['orderDocNo'])
        self.LineEdit_11.setText(self.selRow['customer']['customerName'])
        self.LineEdit_8.setText(self.selRow['customerOrderDocNo'])
        self.LineEdit_9.setText(self.selRow['totalOrderAmount'])
        self.LineEdit_10.setText(self.selRow['employeeName'])
        self.LineEdit_12.setText(self.selRow['tax']['taxContent'])

    def dataResChangeView(self, data):
        self.pageEdit.setValue(data['number'] + 1)
        self.label_2.setText(f'页 共{self.totalPage}页  {self.totalCount}条记录')