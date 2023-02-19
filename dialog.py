from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QDialog

from executor import HttpExecutor, PostThread
from ui.ui_task_form import Ui_TaskForm


class TaskFormDialog(QDialog, Ui_TaskForm, HttpExecutor):
    formCreated = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadDepts()

    def loadDepts(self):
        self.execute_http(
            'getDeptsThread',
            PostThread('https://yj2025.com/ierp/development-pc/v4/process/group?recordStatus=1&keyword='),
            self.deptsResponse
        )
        pass

    @Slot()
    def deptsResponse(self, result):
        self.chejian.clear()
        for d in result['data']:
            self.chejian.addItem(d['departmentName'], d)
        pass

    @Slot()
    def deptSelected(self):
        self.banzu.clear()
        for d in self.chejian.currentData()['children']:
            self.banzu.addItem(d['departmentName'], d)
        pass

    @Slot()
    def accept(self) -> None:
        dict = {
            'chejian_code': self.chejian.currentData()['departmentCode'],
            'chejian_name': self.chejian.currentData()['departmentName'],
            'laxian_name': self.laxian.text(),
            'banzu_code': self.banzu.currentData()['departmentCode'],
            'banzu_name': self.banzu.currentData()['departmentName']
        }
        self.formCreated.emit(dict)
        self.close()
        pass