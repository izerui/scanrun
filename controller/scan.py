import sqlite3
import time

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from ui.ui_scan_frame import Ui_ScanFrame
from utils.db import DbUnit, ScanTableUnit
from utils.executor import HttpExecutor


class ScanFrame(QWidget, Ui_ScanFrame, HttpExecutor):
    returnHome = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def loadData(self):
        scanTableUnit = ScanTableUnit()
        scanTableUnit.deleteAll()
        for i in range(0, 2000):
            dict = {
                'chejian_code': f'chejian_code_{i}',
                'chejian_name': f'chejian_name_{i}',
                'ent_code': 'ent_code_001',
                'business_key': f'business_key_{i}',
                'banzu_code': f'banzu_code_{i}',
                'banzu_name': f'banzu_name_{i}',
                'laxian_name': f'laxian_name_{i}',
                'create_time': time.time(),
                'creator': f'creator_{i}',
                'creator_name': f'creator_name_{i}',
                'unit_code': f'unit_code_{i}',
                'box_code': f'box_code_{i}',
                'pallet_code': f'pallet_code_{i}'
            }
            scanTableUnit.insert(dict)
        list = scanTableUnit.queryForList('SELECT * FROM scan_data')
        for l in list:
            print(l)
            l['chejian_name'] = '修改的内容' + l['chejian_name']
            scanTableUnit.update(l)