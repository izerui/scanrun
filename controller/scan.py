import time
from itertools import groupby
from typing import Callable

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidgetSelectionRange

from ui.ui_scan_frame import Ui_ScanFrame
from utils.context import Context
from utils.db import ScanTableUnit
from utils.executor import HttpExecutor


class ScanFrame(QWidget, Ui_ScanFrame, HttpExecutor):
    returnHome = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.table0.setShowGrid(True)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table0.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.initDemoData()

    # def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
    #     if event.key() == QtCore.Qt.Key.Key_Return.value:
    #         self.scan_code_input.setFocus()
    #         self.scan_code_input.selectAll()

    def setScanInfo(self, order_info):
        self.order_info = order_info
        self.box_inside_quantity = int(self.order_info['boxInsideQuantity'])
        self.pallet_inside_quantity = int(self.order_info['palletInsideQuantity'])
        self.scanTableUnit = ScanTableUnit(
            f'scan_data_{str(self.order_info["saleInventoryRecordId"]).replace("-", "_")}')
        self.renderFormValue()

    # 查询本地数据库的扫码数据
    def loadScanData(self):
        self.refreshCountView()
        self.table0.setRowCount(0)
        self.datas = self.scanTableUnit.queryForList(
            f'SELECT * FROM {self.scanTableUnit.tableName} order by create_time desc')
        if self.datas is None:
            self.datas = []
        self.table0.setRowCount(len(self.datas))
        i = 0
        for d in self.datas:
            self.table0.setItem(i, 0, QTableWidgetItem(d['chejian_name']))
            self.table0.setItem(i, 1, QTableWidgetItem(d['banzu_name']))
            self.table0.setItem(i, 2, QTableWidgetItem(d['creator_name']))
            self.table0.setItem(i, 3, QTableWidgetItem(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(d['create_time'] / 1000))))
            self.table0.setItem(i, 4, QTableWidgetItem(d['unit_code']))
            self.table0.setItem(i, 5, QTableWidgetItem(d['box_code']))
            self.table0.setItem(i, 6, QTableWidgetItem(d['pallet_code']))
            self.table0.setItem(i, 7, QTableWidgetItem(d['upload_status']))
            self.table0.setItem(i, 8, QTableWidgetItem(d['uploader']))
            self.table0.setItem(i, 9, QTableWidgetItem(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(d['upload_time'] / 1000)) if d[
                    'upload_time'] else None))
            i += 1
        self.showWarning()

    # 填充扫码页面的form表单信息
    def renderFormValue(self):
        self.order_no_input.setText(self.order_info['saleOrderDocNo'])
        self.cus_order_no_input.setText(self.order_info['customerOrderDocNo'])
        self.chejian_name_input.setText(self.order_info['chejian_name'])
        self.banzu_name_input.setText(self.order_info['banzu_name'])
        self.task_count_input.setText(str(self.order_info['taskQuantity']))
        self.user_name_input.setText(Context.user['userName'])
        self.inventory_code_input.setText(self.order_info['inventoryCode'])
        self.inventory_name_input.setText(self.order_info['inventoryName'])
        self.unit_rule_label.setText(
            f'规则: 每箱({int(self.order_info["boxInsideQuantity"])})产品 / 每卡板({int(self.order_info["palletInsideQuantity"])})箱')
        pass

    
    def deleteSelection(self):
        for rowIndex, group in groupby(self.tableWidget.selectedIndexes(), lambda x: x.row()):
            print(rowIndex)
            # print(rowIndex, self.datas[rowIndex]['id'])

    
    def tabChanged(self):
        if self.tabWidget.currentIndex() == 0:
            self.loadScanData()
        else:
            self.laodScanedData()

    
    def scan(self):
        if self.tabWidget.currentIndex() > 0:
            self.warn('请切换到未包装列表')
            return
        code = self.scan_code_input.text()
        if not code:
            return
        self.judge(self.insertUnit, self.correlationBox, self.correlationPallet)
        self.scan_code_input.clear()
        self.loadScanData()

    # 判断即将触发的动作
    def judge(self, unitCall: Callable, boxCall: Callable, palletCall: Callable):
        # 一箱数量
        box_quantity = self.box_inside_quantity
        # 一卡板数量
        pallet_quantity = self.pallet_inside_quantity * self.box_inside_quantity
        # 取一箱数据
        box_datas = self.datas[0:box_quantity]
        # 取一卡板数据
        pallet_datas = self.datas[0:pallet_quantity]
        # 未装箱数据
        undo_box_datas = list(filter(lambda x: not x['box_code'], box_datas))
        # 未卡板数据
        undo_pallet_datas = list(filter(lambda x: not x['pallet_code'], pallet_datas))
        # 优先判断卡板，再判断箱子，否则持续录入产品

        if len(undo_box_datas) == box_quantity:  # 够一箱
            boxCall(items=undo_box_datas)
        elif len(undo_pallet_datas) == pallet_quantity:  # 够一卡板
            palletCall(items=undo_pallet_datas)
        else:
            unitCall(items=None)

    # 刷新总计计数
    def refreshCountView(self):
        unit_count = \
            self.scanTableUnit.queryForObject(f'select count(0) as unit_count from {self.scanTableUnit.tableName}')[
                'unit_count']
        box_count = self.scanTableUnit.queryForObject(
            f'select count(distinct box_code) as box_count from {self.scanTableUnit.tableName} where box_code is not null and box_code != \'\'')[
            'box_count']
        pallet_count = self.scanTableUnit.queryForObject(
            f'select count(distinct pallet_code) as pallet_count from {self.scanTableUnit.tableName} where pallet_code is not null and pallet_code != \'\'')[
            'pallet_count']

        self.lcd_unit.setProperty('value', unit_count)
        self.lcd_box.setProperty('value', box_count)
        self.lcd_pallet.setProperty('value', pallet_count)
        pass

    def laodScanedData(self):
        pass

    # 关联装箱
    def correlationBox(self, items: list = None):
        if not items:
            return
        code = self.scan_code_input.text()
        if not code:
            return
        for item in items:
            item['box_code'] = code
            self.scanTableUnit.update(item)

    # 关联装卡板
    def correlationPallet(self, items: list = None):
        if not items:
            return
        code = self.scan_code_input.text()
        if not code:
            return
        for item in items:
            item['pallet_code'] = code
            self.scanTableUnit.update(item)

    # 添加产品
    def insertUnit(self, items: list = None):
        code = self.scan_code_input.text()
        if not code:
            return
        now = int(round(time.time() * 1000))
        # time.strftime('%Y-%m-%d %H:%M%S', time.localtime(now/1000))
        data = {
            'chejian_code': self.order_info['chejian_code'],
            'chejian_name': self.order_info['chejian_name'],
            'ent_code': Context.user['entCode'],
            'business_key': self.order_info['recordId'],
            'banzu_code': self.order_info['banzu_code'],
            'banzu_name': self.order_info['banzu_name'],
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
        self.scanTableUnit.insertIgnore(data)

    
    def unUploadDataSelected(self):
        if self.table0.currentColumn() == 5:
            sel_box_code = self.table0.currentItem().text()
            box_datas = list(filter(lambda x: x['box_code'] == sel_box_code, self.datas))
            if box_datas:
                rect = QTableWidgetSelectionRange(self.datas.index(box_datas[0]), 0,
                                                  self.datas.index(box_datas[len(box_datas) - 1]),
                                                  self.table0.columnCount() - 1)
                self.table0.setRangeSelected(rect, True)
        elif self.table0.currentColumn() == 6:
            sel_pallet_code = self.table0.currentItem().text()
            pallet_datas = list(filter(lambda x: x['pallet_code'] == sel_pallet_code, self.datas))
            if pallet_datas:
                rect = QTableWidgetSelectionRange(self.datas.index(pallet_datas[0]), 0,
                                                  self.datas.index(pallet_datas[len(pallet_datas) - 1]),
                                                  self.table0.columnCount() - 1)
                self.table0.setRangeSelected(rect, True)

    
    def warn(self, message):
        self.warn_label.setText(message)

    def showWarning(self):
        player = QMediaPlayer()
        output = QAudioOutput()
        player.setAudioOutput(output)
        player.setSource(QUrl.fromLocalFile('/Users/liuyuhua/PycharmProjects/scanrun/pic/box.mp3'))
        output.setVolume(50)
        player.play()
        showUnit = lambda items: self.warn_label.setText('请扫描产品')
        showBox = lambda items: self.warn_label.setText('请扫描箱子')
        showPallet = lambda items: self.warn_label.setText('请扫描卡板')
        self.judge(showUnit, showBox, showPallet)
