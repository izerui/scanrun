import time

import PySide6.QtGui
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal, QDateTime, Slot
from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem

from ui.ui_scan_frame import Ui_ScanFrame
from utils.context import Context
from utils.db import ScanTableUnit
from utils.executor import HttpExecutor


class ScanFrame(QWidget, Ui_ScanFrame, HttpExecutor):
    returnHome = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scanTableUnit = ScanTableUnit()
        self.initDemoData()

    # def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
    #     if event.key() == QtCore.Qt.Key.Key_Return.value:
    #         self.scan_code_input.setFocus()
    #         self.scan_code_input.selectAll()

    def initDemoData(self):
        # QDateTime.currentDateTime()
        now = int(round(time.time() * 1000))
        self.scanTableUnit.deleteAll()
        for i in range(0, 2000):
            dict = {
                'chejian_code': f'chejian_code_{i}',
                'chejian_name': f'chejian_name_{i}',
                'ent_code': 'ent_code_001',
                'business_key': f'business_key_{i}',
                'banzu_code': f'banzu_code_{i}',
                'banzu_name': f'banzu_name_{i}',
                'laxian_name': f'laxian_name_{i}',
                'create_time': now,
                'creator': f'creator_{i}',
                'creator_name': f'creator_name_{i}',
                'unit_code': f'unit_code_{i}',
                'box_code': f'box_code_{i}',
                'pallet_code': f'pallet_code_{i}',
                'upload_status': 0,
                'uploader': 'sjdjf',
                'upload_time': QDateTime.currentDateTime()
            }
            self.scanTableUnit.insert(dict)
        list = self.scanTableUnit.queryForList('SELECT * FROM scan_data')
        for l in list:
            print(l)
            l['chejian_name'] = '修改的内容' + l['chejian_name']
            self.scanTableUnit.update(l)

    # 查询本地数据库的已记录扫码数据
    def loadScanData(self, scan_info: dict):
        self.scan_info = scan_info
        self.renderFormValue()
        self.tableWidget.setShowGrid(True)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(0)

        datas = self.scanTableUnit.queryForList('SELECT * FROM scan_data order by create_time desc')
        self.tableWidget.setRowCount(len(datas))
        i = 0
        for d in datas:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(d['chejian_name']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(d['laxian_name']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(d['banzu_name']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(d['create_time']/1000))))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(d['creator']))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(d['unit_code']))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(d['box_code']))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(d['pallet_code']))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(d['upload_status']))
            self.tableWidget.setItem(i, 9, QTableWidgetItem(d['uploader']))
            self.tableWidget.setItem(i, 10, QTableWidgetItem(d['upload_time']))
            i += 1
        # self.tableWidget.show()
        self.tableWidget.selectRow(0)

    # 填充扫码页面的form表单信息
    def renderFormValue(self):
        self.order_no_input.setText(self.scan_info['order_info']['orderDocNo'])
        self.cus_order_no_input.setText(self.scan_info['order_info']['customerOrderDocNo'])
        self.chejian_name_input.setText(self.scan_info['chejian_name'])
        self.laxian_name_input.setText(self.scan_info['laxian_name'])
        self.banzu_name_input.setText(self.scan_info['banzu_name'])
        self.task_count_input.setText(self.scan_info['order_info']['salePlanQuantity'])
        self.user_name_input.setText(Context.user['userName'])
        pass

    @Slot()
    def scan(self):
        now = int(round(time.time() * 1000))
        # time.strftime('%Y-%m-%d %H:%M%S', time.localtime(now/1000))
        code = self.scan_code_input.text()
        if code:
            data = {
                'chejian_code': self.scan_info['chejian_code'],
                'chejian_name': self.scan_info['chejian_name'],
                'ent_code': Context.user['entCode'],
                'business_key': self.scan_info['order_info']['recordId'],
                'banzu_code': self.scan_info['banzu_code'],
                'banzu_name': self.scan_info['banzu_name'],
                'laxian_name': self.scan_info['laxian_name'],
                'create_time': now,
                'creator': Context.user['userCode'],
                'creator_name': Context.user['userName'],
                'unit_code': code,
                'box_code': None,
                'pallet_code': None,
                'upload_status': 0,
                'uploader': None,
                'upload_time': None
            }
            self.scanTableUnit.insert(data)
