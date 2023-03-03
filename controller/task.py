# -*- coding: UTF-8 -*-
from itertools import groupby
from time import sleep

from PySide6.QtCore import Slot, Signal, QItemSelectionModel, Qt
from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit, QLabel, QFormLayout, QCompleter

from controller.dialog import ScanConfirmDialog
from model.TaskModel import TaskModel
from ui.ui_task_frame import Ui_TaskFrame
from utils.context import Context
from utils.executor import HttpExecutor, PostThread


class TaskFrame(QWidget, Ui_TaskFrame, HttpExecutor):
    scanConfirmedSignal = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paging.loadData.connect(self.loadData)

        self.splitter.setSizes([50000, 20000])
        self.renderFormLabels()
        self.selRow = None
        self.firstPage()
        self.autoCompleterEditors = [self.ORDER_DOC_NO, self.CUSTOMER_ORDER_DOC_NO, self.CUSTOMER_MATERIAL, self.CUSTOMER_SERIAL]

    def loadData(self):
        reqParam = {"pageIndex": self.paging.pageIndex, "pageSize": self.paging.pageSize, "total": 0, "completedStatus": False}
        if self.ORDER_DOC_NO.text():
            reqParam['saleOrderDocNo'] = self.ORDER_DOC_NO.text()
        if self.CUSTOMER_ORDER_DOC_NO.text():
            reqParam['customerOrderDocNo'] = self.CUSTOMER_ORDER_DOC_NO.text()
        if self.CUSTOMER_MATERIAL.text():
            reqParam['customerMaterialCode'] = self.CUSTOMER_MATERIAL.text()
        if self.CUSTOMER_SERIAL.text():
            reqParam['customerCode'] = self.CUSTOMER_SERIAL.text()
        self.http('loadDataThread',
                  PostThread(f'{Context.getSettings("gateway/domain")}/ierp/sale-pc/v1/scan/code/task/list',
                             json=reqParam),
                  self.dataResponse
                  )

    def dataResponse(self, result):
        data = result['data']
        self.model = TaskModel(data['content'])
        self.tableView.setModel(self.model)
        self.selectionModel = QItemSelectionModel(self.model)
        self.tableView.setSelectionModel(self.selectionModel)
        self.selectionModel.selectionChanged.connect(self.dataRowSelected)
        self.tableView.selectRow(0)
        self.paging.setPage(data)

    # 行选中事件
    @Slot()
    def dataRowSelected(self, sel, desel):
        group = groupby(sel.indexes(), lambda x: x.row())
        selEndRow = None
        for i, rows in group:
            selEndRow = i
            break
        if selEndRow is None:
            return
        self.selRow = self.model.datas[selEndRow]
        for head in self.model.originHeads:
            if getattr(self, f'form_edit_{head["code"]}'):
                getattr(self, f'form_edit_{head["code"]}').setText(str(self.model.datas[selEndRow][head['code']]))

    @Slot()
    def openTaskForm(self):
        if self.selRow:
            self.task = ScanConfirmDialog(self.selRow)
            # 两个信号连接，直接触发到home
            self.task.scanConfirmedSignal.connect(self.scanConfirmedSignal)
            self.task.show()
        else:
            QMessageBox.warning(None, '提示', '请选择一条任务开始扫码')

    # 初始化表单展示页
    def renderFormLabels(self):
        for i, head in enumerate(TaskModel(None).originHeads):
            label = QLabel(self.scrollAreaWidgetContents)
            label.setObjectName(f'form_label_{head["code"]}')
            label.setText(f'{head["title"]}:')
            edit = QLineEdit(self.scrollAreaWidgetContents)
            edit.setObjectName(f'form_edit_{head["code"]}')
            edit.setReadOnly(True)
            setattr(self, f'form_label_{head["code"]}', label)
            setattr(self, f'form_edit_{head["code"]}', edit)
            self.formLayout_3.addRow(label, edit)
            # self.formLayout_3.setWidget(i, QFormLayout.LabelRole, getattr(self, f'form_edit_{head["code"]}'))
            # self.formLayout_3.setWidget(i, QFormLayout.FieldRole, edit)

        self.show()

    @Slot()
    def completerLineEdit(self):
        print(self.focusWidget().objectName())
        if self.focusWidget() in self.autoCompleterEditors:
            edit:QLineEdit = self.focusWidget()
            text = edit.text() if edit.text() else ''
            search = {"completedStatus": False, "selectType": edit.objectName(), "selectBoxKey": text}
            self.http('orderDocNoComboxThread',
                      PostThread(f'{Context.getSettings("gateway/domain")}/ierp/sale-pc/v1/scan/code/task/select',
                                 json=search), self.orderDocNoComboxResponse)

    def orderDocNoComboxResponse(self, result):
        if self.focusWidget() in self.autoCompleterEditors:
            datas = result['data']
            print(repr(datas))
            if datas is None:
                datas = []
            edit:QLineEdit = self.focusWidget()
            tips = list(map(lambda x: x['label'], datas))
            completer = QCompleter(tips, edit)
            # QCompleter.PopupCompletion 当前完成情况显示在弹出窗口中。
            # QCompleter.InlineCompletion 完成显示为内联（作为选定文本）。
            # QCompleter.UnfilteredPopupCompletion 所有可能的完成都显示在一个弹出窗口中，最有可能的建议被指示为当前。
            completer.setCompletionMode(QCompleter.CompletionMode.UnfilteredPopupCompletion)
            edit.setCompleter(completer)
            completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
            completer.complete()

    @Slot()
    def resetEdits(self):
        for edit in self.autoCompleterEditors:
            edit.clear()
            self.firstPage()
            self.tableView.setFocus()

    @Slot()
    def firstPage(self):
        self.paging.pageIndex = 0
        self.loadData()