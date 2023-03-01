# -*- coding: UTF-8 -*-
from itertools import groupby

from PySide6.QtCore import Slot, QItemSelectionModel, Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QFormLayout, QMessageBox, QCompleter

from model.UploadedModel import UploadedModel
from ui.ui_record_frame import Ui_RecordFrame
from utils.context import Context
from utils.executor import HttpExecutor, PostThread


class RecordFrame(QWidget, Ui_RecordFrame, HttpExecutor):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paging.loadData.connect(self.loadData)
        self.splitter.setSizes([50000, 20000])
        self.renderFormLabels()
        self.selRow = None
        self.firstPage()

    def loadData(self):
        reqParam = {"pageIndex": self.paging.pageIndex, "pageSize": self.paging.pageSize, "total": 0, "activeStatus": "AUDITING",
                    "completedStatus": False}
        if self.ORDER_DOC_NO.text():
            reqParam['saleOrderDocNo'] = self.ORDER_DOC_NO.text()
        if self.CUSTOMER_ORDER_DOC_NO.text():
            reqParam['customerOrderDocNo'] = self.CUSTOMER_ORDER_DOC_NO.text()
        if self.CUSTOMER_MATERIAL.text():
            reqParam['customerMaterialCode'] = self.CUSTOMER_MATERIAL.text()
        if self.CUSTOMER_SERIAL.text():
            reqParam['customerCode'] = self.CUSTOMER_SERIAL.text()
        self.http('loadDataThread',
                  PostThread(f'{Context.getSettings("gateway/domain")}/ierp/sale-pc/v1/scan/code/record/list',
                             json=reqParam),
                  self.dataResponse
                  )

    def dataResponse(self, result):
        data = result['data']
        self.model = UploadedModel(data['content'])
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
        for head in self.model.heads:
            if getattr(self, f'form_edit_{head["code"]}'):
                getattr(self, f'form_edit_{head["code"]}').setText(str(self.model.datas[selEndRow][head['code']]))

    # 初始化表单展示页
    def renderFormLabels(self):
        for i, head in enumerate(UploadedModel(None).heads):
            label = QLabel(self.scrollAreaWidgetContents)
            label.setObjectName(f'form_label_{head["code"]}')
            label.setText(f'{head["title"]}:')
            edit = QLineEdit(self.scrollAreaWidgetContents)
            edit.setObjectName(f'form_edit_{head["code"]}')
            edit.setReadOnly(True)
            self.formLayout_3.setWidget(i, QFormLayout.LabelRole, label)
            self.formLayout_3.setWidget(i, QFormLayout.FieldRole, edit)
            setattr(self, f'form_edit_{head["code"]}', edit)
        self.show()

    @Slot()
    def resetEdits(self):
        for edit in [self.ORDER_DOC_NO, self.CUSTOMER_ORDER_DOC_NO, self.CUSTOMER_MATERIAL, self.CUSTOMER_SERIAL]:
            edit.clear()
            self.firstPage()
            self.tableView.setFocus()

    def firstPage(self):
        self.paging.pageIndex = 0
        self.loadData()

    @Slot()
    def completerLineEdit(self):
        print(self.focusWidget().objectName())
        if self.focusWidget() in [self.ORDER_DOC_NO, self.CUSTOMER_ORDER_DOC_NO, self.CUSTOMER_MATERIAL,
                                  self.CUSTOMER_SERIAL]:
            edit: QLineEdit = self.focusWidget()
            text = edit.text() if edit.text() else ''
            search = {"completedStatus": False, "selectType": edit.objectName(), "selectBoxKey": text}
            self.http('orderDocNoComboxThread',
                      PostThread(f'{Context.getSettings("gateway/domain")}/ierp/sale-pc/v1/scan/code/task/select',
                                 json=search), self.orderDocNoComboxResponse)

    def orderDocNoComboxResponse(self, result):
        if self.focusWidget() in [self.ORDER_DOC_NO, self.CUSTOMER_ORDER_DOC_NO, self.CUSTOMER_MATERIAL,
                                  self.CUSTOMER_SERIAL]:
            datas = result['data']
            print(repr(datas))
            if datas is None:
                datas = []
            edit: QLineEdit = self.focusWidget()
            tips = list(map(lambda x: x['label'], datas))
            completer = QCompleter(tips, edit)
            # QCompleter.PopupCompletion 当前完成情况显示在弹出窗口中。
            # QCompleter.InlineCompletion 完成显示为内联（作为选定文本）。
            # QCompleter.UnfilteredPopupCompletion 所有可能的完成都显示在一个弹出窗口中，最有可能的建议被指示为当前。
            completer.setCompletionMode(QCompleter.CompletionMode.UnfilteredPopupCompletion)
            edit.setCompleter(completer)
            completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
            completer.complete()