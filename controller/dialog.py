from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QDialog, QMessageBox

from utils.context import Context
from utils.executor import HttpExecutor, PostThread
from ui.ui_task_form import Ui_TaskForm


class ScanConfirmDialog(QDialog, Ui_TaskForm, HttpExecutor):
    scanConfirmedSignal = Signal(dict)

    def __init__(self, order_info):
        super().__init__()
        self.setupUi(self)
        self.loadDepts()
        self.order_info = order_info

    def loadDepts(self):
        self.execute(
            'getDeptsThread',
            PostThread(f'{Context.getSettings("gateway/domain")}/ierp/development-pc/v4/process/group?recordStatus=1&keyword='),
            self.deptsResponse
        )

    @Slot()
    def deptsResponse(self, result):
        self.chejian.clear()
        for d in result['data']:
            self.chejian.addItem(d['departmentName'], d)

    @Slot()
    def deptSelected(self):
        self.banzu.clear()
        for d in self.chejian.currentData()['children']:
            self.banzu.addItem(d['departmentName'], d)

    @Slot()
    def accept(self) -> None:
        if not self.banzu.currentData():
            QMessageBox.critical(None, '错误', '请选择班组')
        else:
            self.order_info['box_inside_quantity'] = 10
            self.order_info['pallet_inside_quantity'] = 6
            scan_info = {
                'order_info': self.order_info,
                'chejian_code': self.chejian.currentData()['departmentCode'],
                'chejian_name': self.chejian.currentData()['departmentName'],
                'laxian_name': self.laxian.text(),
                'banzu_code': self.banzu.currentData()['departmentCode'],
                'banzu_name': self.banzu.currentData()['departmentName']
            }
            self.scanConfirmedSignal.emit(scan_info)
            self.close()