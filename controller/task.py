from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget, QHeaderView, QMessageBox, QTableWidgetItem, QAbstractItemView

from controller.dialog import ScanConfirmDialog
from controller.task_model import TaskModel
from utils.context import Context
from utils.executor import HttpExecutor, PostThread
from ui.ui_task_frame import Ui_TaskFrame


class TaskFrame(QWidget, Ui_TaskFrame, HttpExecutor):
    scanConfirmedSignal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.tableView.selectionModel().selectionChanged.connect(self.dataRowSelected)

        self.model = TaskModel(self.tableView)
        self.tableView.setModel(self.model)
        self.tableView.setShowGrid(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.pageIndex = 0
        self.pageSize = 20
        self.totalPage = 0
        self.totalCount = 0
        self.firstPage()

    def loadData(self):
        reqParam = {"pageIndex": 0, "pageSize": 20, "total": 0, "activeStatus": "AUDITING", "completedStatus": False}
        self.execute('loadDataThread',
                     PostThread(f'{Context.getSettings("gateway/domain")}/ierp/sale-pc/v1/scan/code/task/list',
                                json=reqParam),
                     self.dataResponse
                     )

    def dataResponse(self, result):
        data = result['data']
        self.wrapPageData(data)
        self.dataResChangeView(data)
        # self.model.clear()
        # self.model = QStandardItemModel()
        # self.model.setRowCount(len(data['content']))
        # self.tableView.setRowCount(len(data['content']))
        # i = 0
        self.model.setRowDatas(data['content'])
        self.tableView.selectRow(0)

    def wrapPageData(self, data):
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
        selRow = self.model.currentSelectedRow()
        if selRow:
            self.task = ScanConfirmDialog(selRow)
            # 两个信号连接，直接触发到home
            self.task.scanConfirmedSignal.connect(self.scanConfirmedSignal)
            self.task.show()
        else:
            QMessageBox.warning(None, '提示', '请选择一条任务开始扫码')

    @Slot()
    def dataRowSelected(self):
        self.selRow = self.dataList[self.tableView.currentRow() - 1]
        self.LineEdit_7.setText(self.selRow['orderDocNo'])
        self.LineEdit_11.setText(self.selRow['customer']['customerName'])
        self.LineEdit_8.setText(self.selRow['customerOrderDocNo'])
        self.LineEdit_9.setText(self.selRow['inventoryAmount'])
        self.LineEdit_10.setText(self.selRow['employeeName'])
        self.LineEdit_12.setText(self.selRow['unitPrice'])

    def dataResChangeView(self, data):
        self.pageEdit.setValue(data['number'] + 1)
        self.label_2.setText(f'页 共{self.totalPage}页  {self.totalCount}条记录')


