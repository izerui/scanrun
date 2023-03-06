# -*- coding: UTF-8 -*-
import logging
import os
import random
import string
import time
from itertools import groupby
from typing import Callable

import simpleaudio as sa
from PySide6.QtCore import Signal, Slot, QItemSelectionModel, QItemSelection
from PySide6.QtWidgets import QWidget, QTableView, QMessageBox

from action.upload import UploadAction
from controller.component import ConfirmMessageBox
from model.ScanModel import ScanModel
from model.em import ScanType
from ui.ui_scan_frame import Ui_ScanFrame
from utils.context import Context
from utils.db import ScanTableUnit
from utils.executor import HttpExecutor, ThreadExecutor, SoundThread


class ScanFrame(QWidget, Ui_ScanFrame, HttpExecutor, ThreadExecutor):
    returnHome = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.continuePrompt = True
        try:
            self.errorSound = sa.WaveObject.from_wave_file(f'{os.getcwd()}{os.sep}media{os.sep}error.wav')
            self.unitSound = sa.WaveObject.from_wave_file(f'{os.getcwd()}{os.sep}media{os.sep}unit.wav')
            self.boxSound = sa.WaveObject.from_wave_file(f'{os.getcwd()}{os.sep}media{os.sep}box.wav')
            self.palletSound = sa.WaveObject.from_wave_file(f'{os.getcwd()}{os.sep}media{os.sep}pallet.wav')
        except Exception as e:
            logging.error(e)

    # def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
    #     if event.key() == QtCore.Qt.Key.Key_Return.value:
    #         self.scan_code_input.setFocus()
    #         self.scan_code_input.selectAll()

    def initScanInfo(self, order_info):
        self.order_info = order_info
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(int(self.order_info['taskQuantity']))
        self.box_inside_quantity = int(self.order_info['boxInsideQuantity'])
        self.pallet_inside_quantity = int(self.order_info['palletInsideQuantity'])
        self.scanTableUnit = ScanTableUnit(
            f'scan_data_{str(self.order_info["saleInventoryRecordId"]).replace("-", "_")}')
        self.renderFormValue()
        self.tabWidget.setCurrentIndex(0)

    # 填充扫码页面的form表单信息
    def renderFormValue(self):
        self.order_no_input.setText(self.order_info['saleOrderDocNo'])
        self.cus_order_no_input.setText(self.order_info['customerOrderDocNo'])
        self.chejian_name_input.setText(self.order_info['chejian_name'])
        self.banzu_name_input.setText(self.order_info['banzu_name'])
        self.task_count_input.setText(str(int(self.order_info['taskQuantity'])))
        self.user_name_input.setText(Context.user.userName)
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
        confirm = ConfirmMessageBox('确认', '确认删除选中的数据?')
        confirm.show(lambda: (
            self.scanTableUnit.deleteByIds(selIds),
            self.tabChanged()
        ))

    def getSelectionIds(self) -> list:
        selIds = []
        for rowIndex, group in groupby(self.currentTable().selectedIndexes(), lambda x: x.row()):
            selIds.append(self.model.datas[rowIndex]['id'])
        return selIds

    @Slot()
    def tabChanged(self):
        if self.tabWidget.currentIndex() == 0:
            self.loadData(0)
        else:
            self.loadData(1)

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
        self.loadData(0)

    # 判断即将触发的动作
    def judge(self, unitCall: Callable, boxCall: Callable, palletCall: Callable):
        # 一箱数量
        box_quantity = self.box_inside_quantity
        # 一卡板数量
        pallet_quantity = self.pallet_inside_quantity * self.box_inside_quantity
        # 取一箱数据
        box_datas = self.model.datas[0:box_quantity]
        # 取一卡板数据
        pallet_datas = self.model.datas[0:pallet_quantity]
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
        self.scan_unit_count = self.scanTableUnit.queryForObject(
            f'select count(0) as unit_count from {self.scanTableUnit.tableName}')
        self.scan_box_count = self.scanTableUnit.queryForObject(
            f'select count(distinct box_code) as box_count from {self.scanTableUnit.tableName} where box_code is not null and box_code != \'\'')
        self.scan_pallet_count = self.scanTableUnit.queryForObject(
            f'select count(distinct pallet_code) as pallet_count from {self.scanTableUnit.tableName} where pallet_code is not null and pallet_code != \'\'')

        self.lcd_unit.setProperty('value', self.scan_unit_count)
        self.lcd_box.setProperty('value', self.scan_box_count)
        self.lcd_pallet.setProperty('value', self.scan_pallet_count)
        if self.scan_unit_count <= self.progressBar.maximum():
            self.progressBar.setValue(self.scan_unit_count)
        else:
            self.progressBar.setValue(self.progressBar.maximum())

    def loadData(self, complete):
        self.refreshCountView()
        _datas = self.scanTableUnit.queryForList(
            f'SELECT * FROM {self.scanTableUnit.tableName} where complete = {complete} order by create_time desc'
        )
        self.model = ScanModel(complete, _datas)
        self.currentTable().setModel(self.model)

        self.tableSelectionModel = QItemSelectionModel(self.model)
        self.currentTable().setSelectionModel(self.tableSelectionModel)
        self.tableSelectionModel.selectionChanged.connect(self.selectionChanged)
        # 如果是扫码列表页面，则进行下一步提示
        if complete == 0:
            self.nextPrompt()
            self.scan_code_input.setFocus()
            self.scan_code_input.selectAll()

    @Slot()
    def selectionChanged(self, sel: QItemSelection, desel: QItemSelection):
        group = groupby(sel.indexes(), lambda x: x.row())
        for i, rows in group:
            # print(self.model.datas[i])
            pass
        pass

    def validateCode(self, currentType: ScanType, code) -> bool:
        if not code:
            self.warn()
            return False
        exist_unit_count = self.scanTableUnit.queryForObject(
            f'select count(0) as exist_unit_count from {self.scanTableUnit.tableName} where unit_code = :code',
            {'code': code})
        exist_box_count = self.scanTableUnit.queryForObject(
            f'select count(0) as exist_box_count from {self.scanTableUnit.tableName} where box_code = :code',
            {'code': code})
        exist_pallet_count = self.scanTableUnit.queryForObject(
            f'select count(0) as exist_pallet_count from {self.scanTableUnit.tableName} where pallet_code = :code',
            {'code': code})
        if exist_unit_count > 0:
            self.warn(f'{currentType.value["typeName"]}在产品码已存在')
        elif exist_box_count > 0:
            self.warn(f'{currentType.value["typeName"]}在箱码已存在')
        elif exist_pallet_count > 0:
            self.warn(f'{currentType.value["typeName"]}在卡板码已存在')
        else:
            return True
        # 异常后，不需要下一步提示
        self.continuePrompt = False
        return False

    # 关联装箱
    def correlationBox(self, items: list = None):
        code = self.scan_code_input.text()
        if not self.validateCode(ScanType.box, code):
            return
        for item in items:
            item['box_code'] = code
            self.scanTableUnit.update(item)

    # 关联装卡板
    def correlationPallet(self, items: list = None):
        code = self.scan_code_input.text()
        if not self.validateCode(ScanType.pallet, code):
            return
        for item in items:
            item['complete'] = 1
            item['pallet_code'] = code
            self.scanTableUnit.update(item)
        # 任务数量已足够，提示
        if int(self.lcd_unit.value()) >= int(self.order_info['taskQuantity']):
            QMessageBox.information(None, '提示', '扫描任务数量已完成')

    # 添加产品
    def insertUnit(self, items: list = None):
        code = self.scan_code_input.text()
        if not self.validateCode(ScanType.unit, code):
            return
        now = int(round(time.time() * 1000))
        # time.strftime('%Y-%m-%d %H:%M%S', time.localtime(now/1000))
        data = {
            'chejian_code': self.order_info['chejian_code'],
            'chejian_name': self.order_info['chejian_name'],
            'ent_code': Context.user.entCode,
            'business_key': self.order_info['recordId'],
            'banzu_code': self.order_info['banzu_code'],
            'banzu_name': self.order_info['banzu_name'],
            'create_time': now,
            'creator': Context.user.userCode,
            'creator_name': Context.user.userName,
            'unit_code': code,
            'box_code': '',
            'pallet_code': '',
            'complete': 0,
            'upload_status': 0,
            'uploader': '',
            'uploader_name': '',
            'upload_time': ''
        }
        self.scanTableUnit.insertIgnore(data)

    # 获取当前的table0、table1
    def currentTable(self) -> QTableView:
        return getattr(self, f'tableView{self.tabWidget.currentIndex()}')

    # @Slot()
    # def tableItemSelected(self):
    #     currentTable = self.currentTable()
    #     if currentTable.currentColumn() == 5:
    #         sel_box_code = currentTable.currentItem().text()
    #         box_datas = list(filter(lambda x: x['box_code'] == sel_box_code, self.model.datas))
    #         if box_datas:
    #             rect = QTableWidgetSelectionRange(self.model.datas.index(box_datas[0]), 0,
    #                                               self.model.datas.index(box_datas[len(box_datas) - 1]),
    #                                               currentTable.columnCount() - 1)
    #             currentTable.setRangeSelected(rect, True)
    #     elif currentTable.currentColumn() == 6:
    #         sel_pallet_code = currentTable.currentItem().text()
    #         pallet_datas = list(filter(lambda x: x['pallet_code'] == sel_pallet_code, self.model.datas))
    #         if pallet_datas:
    #             rect = QTableWidgetSelectionRange(self.model.datas.index(pallet_datas[0]), 0,
    #                                               self.model.datas.index(pallet_datas[len(pallet_datas) - 1]),
    #                                               currentTable.columnCount() - 1)
    #             currentTable.setRangeSelected(rect, True)

    def tip(self, message):
        self.warn_label.setText(message)

    def warn(self, message=None):
        if message:
            self.warn_label.setText(message)
        self.runAsync('errorSoundThread', SoundThread(self.errorSound))

    # 下一步提示
    def nextPrompt(self):
        # 如果不需要继续提示则忽略下面的提示
        if not self.continuePrompt:
            self.continuePrompt = True
            return

        def showUnit(items=None):
            self.tip('请扫描产品')
            self.runAsync('unitSoundThread', SoundThread(self.unitSound))

        def showBox(items=None):
            self.tip('请扫描箱子')
            self.runAsync('boxSoundThread', SoundThread(self.boxSound))

        def showPallet(items=None):
            self.tip('请扫描卡板')
            self.runAsync('palletSoundThread', SoundThread(self.palletSound))

        self.judge(showUnit, showBox, showPallet)
        autoCode = Context.getSettings('scan/auto_code')
        if autoCode and str(autoCode) == 'true':
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            self.scan_code_input.setText(ran_str)

    @Slot()
    def uploadItems(self):
        def call():
            self.uploadAction = UploadAction(self.model, self.order_info, self.scanTableUnit, self.progressBar)
            self.uploadAction.start()

        confirm = ConfirmMessageBox('确认', '开始上传数据?')
        confirm.show(call)
