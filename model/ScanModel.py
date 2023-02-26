import time
from typing import Union, Any

import PySide6.QtCore
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


class ScanModel(QtCore.QAbstractTableModel):

    def __init__(self, datas):
        super().__init__()
        self.heads = [
            {'title': '车间', 'code': 'chejian_name'},
            {'title': '班组', 'code': 'banzu_name'},
            {'title': '操作人', 'code': 'creator'},
            {'title': '扫码时间', 'code': 'create_time', 'label_format_fun': self.date_time_fun},
            {'title': '产品码', 'code': 'unit_code'},
            {'title': '箱玛', 'code': 'box_code'},
            {'title': '卡板码', 'code': 'pallet_code'},
            {'title': '上传状态', 'code': 'upload_status', 'label_hidden': True, 'icon_fun': self.upload_icon_fun},
            {'title': '上传人', 'code': 'uploader'},
            {'title': '上传时间', 'code': 'upload_time'}
        ]
        self.datas = []
        for d in datas:
            self.datas.append(d)

    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> Any:
        if role == QtCore.Qt.DisplayRole:
            if orientation == PySide6.QtCore.Qt.Orientation.Horizontal:
                return self.heads[section]['title']
            else:
                return str(section + 1)

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex],
             role: int = ...) -> Any:
        row = index.row()
        col = index.column()
        item = self.datas[row]
        key = self.heads[col]['code']
        if role == Qt.DisplayRole:
            if 'label_hidden' in self.heads[col] and self.heads[col]['label_hidden']:
                return None
            else:
                if 'label_format_fun' in self.heads[col]:
                    label_format_fun = self.heads[col]['label_format_fun']
                    return label_format_fun(key, item)
                else:
                    return str(item[key])
        elif role == Qt.DecorationRole:
            if 'icon_fun' in self.heads[col]:
                icon_fun = self.heads[col]['icon_fun']
                return icon_fun(key, item)

    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.heads)

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.datas)

    def upload_icon_fun(self, key, item) -> QIcon:
        return QtGui.QIcon(':/logo/pic/yes.png') if item['upload_status'] and item[
            'upload_status'] == 1 else QtGui.QIcon(':/logo/pic/no.png')

    def date_time_fun(self, key, item) -> str:
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item[key] / 1000)) if item[key] else None