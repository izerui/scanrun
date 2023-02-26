from typing import Union, Any

import PySide6.QtCore
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt

class ScanModel(QtCore.QAbstractTableModel):
    heads = [
        {'title': '车间', 'code': 'chejian_name'},
        {'title': '班组', 'code': 'banzu_name'},
        {'title': '操作人', 'code': 'creator'},
        {'title': '扫码时间', 'code': 'create_time'},
        {'title': '产品码', 'code': 'unit_code'},
        {'title': '箱玛', 'code': 'box_code'},
        {'title': '卡板码', 'code': 'pallet_code'},
        {'title': '上传状态', 'code': 'upload_status'},
        {'title': '上传人', 'code': 'uploader'},
        {'title': '上传时间', 'code': 'upload_time'}
    ]

    def __init__(self, datas):
        super().__init__()
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
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            if col == 7:
                return None
            else:
                return str(self.datas[row][self.heads[col]['code']])
        elif role == Qt.DecorationRole:
            if index.column() == 7:
                return QtGui.QIcon(':/logo/pic/yes.png')



    def columnCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.heads)

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.datas)


