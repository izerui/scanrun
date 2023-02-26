# -*- coding: UTF-8 -*-
import os
import time
from itertools import groupby
from typing import Callable

from PySide6 import QtGui
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidgetSelectionRange, QTableWidget, QMessageBox

from ui.ui_scan_frame import Ui_ScanFrame
from utils.context import Context
from utils.db import ScanTableUnit
from utils.executor import HttpExecutor, ThreadExecutor, SoundThread


class ScanFrame(QWidget, Ui_ScanFrame, HttpExecutor):
    returnHome = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.threadExecutor = ThreadExecutor()
        self.unitSoundThread = SoundThread(f'{os.sep}pic{os.sep}unit.mp3')
        self.boxSoundThread = SoundThread(f'{os.sep}pic{os.sep}box.wav')
        self.palletSoundThread = SoundThread(f'{os.sep}pic{os.sep}pallet.mp3')
        self.errorSoundThread = SoundThread(f'{os.sep}pic{os.sep}error.mp3')
        self.continuePrompt = True
        self.table0.setShowGrid(True)

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
            f'SELECT * FROM {self.scanTableUnit.tableName} where complete = 0 order by create_time desc')
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
            i += 1
        self.nextPrompt()

    # 填充扫码页面的form表单信息
    def renderFormValue(self):
        self.order_no_input.setText(self.order_info['saleOrderDocNo'])
        self.cus_order_no_input.setText(self.order_info['customerOrderDocNo'])
        self.chejian_name_input.setText(self.order_info['chejian_name'])
        self.banzu_name_input.setText(self.order_info['banzu_name'])
        self.task_count_input.setText(str(int(self.order_info['taskQuantity'])))
        self.user_name_input.setText(Context.user['userName'])
        self.inventory_code_input.setText(self.order_info['inventoryCode'])
        self.inventory_name_input.setText(self.order_info['inventoryName'])
        self.unit_rule_label.setText(
            f'规则: 每箱({int(self.order_info["boxInsideQuantity"])})产品 / 每卡板({int(self.order_info["palletInsideQuantity"])})箱')
        pass

    @Slot()
    def deleteSelection(self):
        selIds = self.getSelectionIds()
        if not selIds:
            return
        choiceBox = QMessageBox()
        choiceBox.setIcon(QMessageBox.Icon.Question)
        choiceBox.setWindowTitle('确认')
        choiceBox.setText('确认删除选择的数据')
        yes = choiceBox.addButton('确认', QMessageBox.ButtonRole.YesRole)
        yes.setFocus()
        no = choiceBox.addButton('取消', QMessageBox.ButtonRole.NoRole)
        choiceBox.setDefaultButton(yes)
        choiceBox.exec()
        if choiceBox.clickedButton() == yes:
            self.scanTableUnit.deleteByIds(selIds)
            self.tabChanged()

    def getSelectionIds(self) -> list:
        selIds = []
        for rowIndex, group in groupby(self.currentTable().selectedIndexes(), lambda x: x.row()):
            selIds.append(self.datas[rowIndex]['id'])
        return selIds

    @Slot()
    def tabChanged(self):
        if self.tabWidget.currentIndex() == 0:
            self.scan_code_input.setFocus()
            self.loadScanData()
        else:
            self.laodScanedData()

    @Slot()
    def scan(self):
        if self.tabWidget.currentIndex() > 0:
            self.warn('请切换到未包装列表')
            return
        code = self.scan_code_input.text()
        if not code:
            self.warn()
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
        if len(undo_box_datas) > 0 and len(undo_box_datas) == box_quantity:  # 够一箱
            boxCall(items=undo_box_datas)
        elif len(undo_pallet_datas) > 0 and len(undo_pallet_datas) == pallet_quantity:  # 够一卡板
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
        self.refreshCountView()
        self.table1.setRowCount(0)
        self.datas = self.scanTableUnit.queryForList(
            f'SELECT * FROM {self.scanTableUnit.tableName} where complete = 1 order by create_time desc')
        if self.datas is None:
            self.datas = []
        self.table1.setRowCount(len(self.datas))
        i = 0
        for d in self.datas:
            self.table1.setItem(i, 0, QTableWidgetItem(d['chejian_name']))
            self.table1.setItem(i, 1, QTableWidgetItem(d['banzu_name']))
            self.table1.setItem(i, 2, QTableWidgetItem(d['creator_name']))
            self.table1.setItem(i, 3, QTableWidgetItem(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(d['create_time'] / 1000))))
            self.table1.setItem(i, 4, QTableWidgetItem(d['unit_code']))
            self.table1.setItem(i, 5, QTableWidgetItem(d['box_code']))
            self.table1.setItem(i, 6, QTableWidgetItem(d['pallet_code']))
            self.table1.setItem(i, 7, QTableWidgetItem(d['upload_status']))
            self.table1.setItem(i, 8, QTableWidgetItem(d['uploader']))
            self.table1.setItem(i, 9, QTableWidgetItem(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(d['upload_time'] / 1000)) if d[
                    'upload_time'] else None))
            i += 1

    def validateCode(self, code) -> bool:
        if not code:
            self.warn()
            return False
        exist_unit_count = self.scanTableUnit.queryForObject(
            f'select count(0) as exist_unit_count from {self.scanTableUnit.tableName} where unit_code = :code',
            {'code': code})['exist_unit_count']
        exist_box_count = self.scanTableUnit.queryForObject(
            f'select count(0) as exist_box_count from {self.scanTableUnit.tableName} where box_code = :code',
            {'code': code})['exist_box_count']
        exist_pallet_count = self.scanTableUnit.queryForObject(
            f'select count(0) as exist_pallet_count from {self.scanTableUnit.tableName} where pallet_code = :code',
            {'code': code})['exist_pallet_count']
        if exist_unit_count > 0:
            self.warn('产品码已存在')
        elif exist_box_count > 0:
            self.warn('箱码已存在')
        elif exist_pallet_count > 0:
            self.warn('卡板码已存在')
        else:
            return True
        # 异常后，不需要下一步提示
        self.continuePrompt = False
        return False

    # 关联装箱
    def correlationBox(self, items: list = None):
        code = self.scan_code_input.text()
        if not self.validateCode(code):
            return
        for item in items:
            item['box_code'] = code
            self.scanTableUnit.update(item)

    # 关联装卡板
    def correlationPallet(self, items: list = None):
        code = self.scan_code_input.text()
        if not self.validateCode(code):
            return
        for item in items:
            item['complete'] = 1
            item['pallet_code'] = code
            self.scanTableUnit.update(item)

    # 添加产品
    def insertUnit(self, items: list = None):
        code = self.scan_code_input.text()
        if not self.validateCode(code):
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
            'complete': 0,
            'upload_status': 0,
            'uploader': None,
            'upload_time': None
        }
        self.scanTableUnit.insertIgnore(data)

    # 获取当前的table0、table1
    def currentTable(self) -> QTableWidget:
        return getattr(self, f'table{self.tabWidget.currentIndex()}')

    @Slot()
    def tableItemSelected(self):
        currentTable = self.currentTable()
        if currentTable.currentColumn() == 5:
            sel_box_code = currentTable.currentItem().text()
            box_datas = list(filter(lambda x: x['box_code'] == sel_box_code, self.datas))
            if box_datas:
                rect = QTableWidgetSelectionRange(self.datas.index(box_datas[0]), 0,
                                                  self.datas.index(box_datas[len(box_datas) - 1]),
                                                  currentTable.columnCount() - 1)
                currentTable.setRangeSelected(rect, True)
        elif currentTable.currentColumn() == 6:
            sel_pallet_code = currentTable.currentItem().text()
            pallet_datas = list(filter(lambda x: x['pallet_code'] == sel_pallet_code, self.datas))
            if pallet_datas:
                rect = QTableWidgetSelectionRange(self.datas.index(pallet_datas[0]), 0,
                                                  self.datas.index(pallet_datas[len(pallet_datas) - 1]),
                                                  currentTable.columnCount() - 1)
                currentTable.setRangeSelected(rect, True)

    def tip(self, message):
        self.warn_label.setText(message)

    def warn(self, message=None):
        if message:
            self.warn_label.setText(message)
        if not self.errorSoundThread.isRunning():
            self.errorSoundThread.start()

    # 下一步提示
    def nextPrompt(self):
        # 如果不需要继续提示则忽略下面的提示
        if not self.continuePrompt:
            self.continuePrompt = True
            return

        def showUnit(items=None):
            self.tip('请扫描产品')
            if not self.unitSoundThread.isRunning():
                self.unitSoundThread.start()

        def showBox(items=None):
            self.tip('请扫描箱子')
            if not self.boxSoundThread.isRunning():
                self.boxSoundThread.start()

        def showPallet(items=None):
            self.tip('请扫描卡板')
            if not self.palletSoundThread.isRunning():
                self.palletSoundThread.start()

        self.judge(showUnit, showBox, showPallet)

    @Slot()
    def uploadItems(self):
        pass
