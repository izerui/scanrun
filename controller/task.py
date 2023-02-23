from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget, QHeaderView, QMessageBox, QTableWidgetItem, QLabel, QFormLayout, QLineEdit

from controller.dialog import ScanConfirmDialog
from utils.context import Context
from utils.executor import HttpExecutor, PostThread
from ui.ui_task_frame import Ui_TaskFrame


class TaskFrame(QWidget, Ui_TaskFrame, HttpExecutor):
    scanConfirmedSignal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pageIndex = 0
        self.pageSize = 20
        self.totalPage = 0
        self.totalCount = 0
        self.firstPage()

    def loadData(self):
        self.tableWidget.setShowGrid(True)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
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
            for j, head in enumerate(TaskFrame.heads):
                self.tableWidget.setItem(i, j, QTableWidgetItem(d[head['code']]))
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

    @Slot()
    def dataRowSelected(self):
        self.selRow = self.dataList[self.tableWidget.currentRow() - 1]
        for head in TaskFrame.heads:
            getattr(self, head['code']).setText(str(self.selRow[head['code']]))

    def dataResChangeView(self, data):
        self.pageEdit.setValue(data['number'] + 1)
        self.label_2.setText(f'页 共{self.totalPage}页  {self.totalCount}条记录')

    heads = [{
            'title': "销售单号",
            'code': "saleOrderDocNo"
        },
            {
                'title': "客户编码",
                'code': "customerSerial"
            },
            {
                'title': "客户名称",
                'code': "customerName"
            },
            {
                'title': "客户订单号",
                'code': "customerOrderDocNo"
            },
            {
                'title': "货品编码",
                'code': "inventoryCode"
            },
            {
                'title': "货品名称",
                'code': "inventoryName"
            },
            {
                'title': "规格型号",
                'code': "inventorySpec"
            },
            {
                'title': "单位",
                'code': "unitName"
            },
            {
                'title': "客户料号",
                'code': "customerMaterialCode"
            },
            {
                'title': "客户品名",
                'code': "customerInventoryName"
            },
            {
                'title': "客户型号",
                'code': "customerInventorySpec"
            },
            {
                'title': "业务员",
                'code': "employeeName"
            },
            {
                'title': "任务创建人",
                'code': "creatorName"
            },
            {
                'title': "任务创建日期",
                'code': "createTime"
            },
            {
                'title': "订单交期",
                'code': "deliveryDate"
            },
            {
                'title': "销售订单数量",
                'code': "quantity"
            },
            {
                'title': "任务数量",
                'code': "taskQuantity"
            },
            {
                'title': "已扫码数量",
                'code': "scanCodeQuantity"
            },
            {
                'title': "未扫码数量",
                'code': "waitScanCodeQuantity"
            },
            {
                'title': "装箱数量",
                'code': "boxQuantity"
            },
            {
                'title': "卡板数量",
                'code': "palletQuantity"
            }
        ]
