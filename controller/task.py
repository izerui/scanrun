# -*- coding: UTF-8 -*-
from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QLineEdit, QLabel, QFormLayout

from controller.dialog import ScanConfirmDialog
from ui.ui_task_frame import Ui_TaskFrame
from utils.context import Context
from utils.executor import HttpExecutor, PostThread


class TaskFrame(QWidget, Ui_TaskFrame, HttpExecutor):
    scanConfirmedSignal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.splitter.setSizes([50000, 20000])
        self.renderTable()
        self.renderFormLabels()
        self.pageIndex = 0
        self.pageSize = 20
        self.totalPage = 0
        self.totalCount = 0
        self.firstPage()

    def loadData(self):
        self.tableWidget.setRowCount(0)
        reqParam = {"pageIndex": self.pageIndex, "pageSize": self.pageSize, "total": 0, "activeStatus": "AUDITING",
                    "completedStatus": False}
        self.execute('loadDataThread',
                     PostThread(f'{Context.getSettings("gateway/domain")}/ierp/sale-pc/v1/scan/code/task/list',
                                json=reqParam),
                     self.dataResponse
                     )

    def dataResponse(self, result):
        data = result['data']
        self.wrapPageData(data)
        self.dataResChangeView(data)
        self.tableWidget.setRowCount(len(data['content']))
        i = 0
        for d in data['content']:
            j = 0
            for head in Context.todoTaskTableHeads:
                if ('hide' not in head or not head['hide']):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(d[head['code']]))
                    j += 1
            i += 1
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
            self.task = ScanConfirmDialog(self.selRow)
            # 两个信号连接，直接触发到home
            self.task.scanConfirmedSignal.connect(self.scanConfirmedSignal)
            self.task.show()
        else:
            QMessageBox.warning(None, '提示', '请选择一条任务开始扫码')

    # 行选中事件
    @Slot()
    def dataRowSelected(self):
        self.selRow = self.dataList[self.tableWidget.currentRow() - 1]
        for head in Context.todoTaskTableHeads:
            if getattr(self, f'form_edit_{head["code"]}'):
                getattr(self, f'form_edit_{head["code"]}').setText(str(self.selRow[head['code']]))

    def dataResChangeView(self, data):
        self.pageEdit.setValue(data['number'] + 1)
        self.label_2.setText(f'页 共{self.totalPage}页  {self.totalCount}条记录')

    # 初始化表格列头及样式
    def renderTable(self):
        self.tableWidget.setShowGrid(True)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(list(filter(lambda x: 'hide' not in x or not x['hide'], Context.todoTaskTableHeads))))
        i = 0
        for head in Context.todoTaskTableHeads:
            if not head.get('hide'):
                self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(head.get('title')))
                i += 1

    # 初始化表单展示页
    def renderFormLabels(self):
        for i, head in enumerate(Context.todoTaskTableHeads):
            label = QLabel(self.scrollAreaWidgetContents)
            label.setObjectName(f'form_label_{head["code"]}')
            label.setText(f'{head["title"]}:')
            edit = QLineEdit(self.scrollAreaWidgetContents)
            edit.setObjectName(f'form_edit_{head["code"]}')
            edit.setReadOnly(True)
            self.formLayout_3.setWidget(i, QFormLayout.LabelRole, label)
            self.formLayout_3.setWidget(i, QFormLayout.FieldRole, edit)
            setattr(self, f'form_edit_{head["code"]}', edit)
        self.formLayout_3.update()