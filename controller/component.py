from typing import Callable

from PySide6.QtCore import Signal, Slot, QDate
from PySide6.QtWidgets import QMessageBox, QWidget

from ui.ui_date_range import Ui_DateRange
from ui.ui_paging import Ui_PagingWidget


# 确认对话框
class ConfirmMessageBox(QMessageBox):

    def __init__(self, title, message):
        super().__init__()
        self.setIcon(QMessageBox.Icon.Question)
        self.setWindowTitle(title)
        self.setText(message)
        self.yes = self.addButton('确认', QMessageBox.ButtonRole.YesRole)
        self.yes.setFocus()
        self.no = self.addButton('取消', QMessageBox.ButtonRole.NoRole)
        self.setDefaultButton(self.yes)

    def show(self, success: Callable) -> int:
        exe = super().exec()
        if self.clickedButton() == self.yes:
            success()
        return exe


# 分页组件
class PagingWidget(QWidget, Ui_PagingWidget):
    loadData = Signal()

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.pageIndex = 0
        self.pageSize = 20
        self.totalPage = 0
        self.totalCount = 0

    def setPage(self, data: dict):
        self.pageIndex = data['number']
        self.totalPage = data['totalPages']
        self.totalCount = data['totalElements']
        self.pageSize = data['size']
        self.pageEdit.setValue(data['number'] + 1)
        self.label_2.setText(f'共 {self.totalCount}条 {self.totalPage}页')

    @Slot()
    def firstPage(self):
        self.pageIndex = 0
        self.loadData.emit()

    @Slot()
    def prePage(self):
        if self.pageIndex > 0:
            self.pageIndex -= 1
            self.loadData.emit()
        else:
            QMessageBox.warning(None, '提示', '已经是第一页')

    @Slot()
    def nextPage(self):
        if self.pageIndex + 1 < self.totalPage:
            self.pageIndex += 1
            self.loadData.emit()
        else:
            QMessageBox.warning(None, '提示', '已经是最后一页')

    @Slot()
    def endPage(self):
        if self.totalPage - 1 > 0:
            self.pageIndex = self.totalPage - 1
        self.loadData.emit()

    @Slot()
    def jumpPage(self):
        if self.pageEdit.value() >= self.totalPage:
            self.pageIndex = self.totalPage - 1
        else:
            self.pageIndex = self.pageEdit.value() - 1
        self.loadData.emit()


class DateRange(QWidget, Ui_DateRange):
    dateRangeSignal = Signal(QDate, QDate)

    def __init__(self, layout=None):
        super().__init__()
        self.setupUi(self)
        self.resetDate()

    @Slot()
    def beginChanged(self):
        self.end.setFocus()
        # self.end.calendarWidget().show()
        pass

    @Slot()
    def endChanged(self):
        beginDate = self.begin.date().toPython()
        endDate = self.end.date().toPython()
        if beginDate and endDate:
            self.dateRangeSignal.emit(beginDate, endDate)

    def isValid(self) -> bool:
        if self.begin.date() and self.end.date():
            return True
        return False

    def resetDate(self):
        self.begin.setDate(QDate.currentDate())
        self.end.setDate(QDate.currentDate())