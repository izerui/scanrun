from enum import Enum


class ScanType(Enum):
    unit = {
        'type': 'unit',
        'typeName': '产品码'
    }
    box = {
        'type': 'box',
        'typeName': '纸箱码'
    }
    pallet = {
        'type': 'pallet',
        'typeName': '卡板码'
    }