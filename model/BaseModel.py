import time
from typing import Union, Any

import PySide6.QtCore
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


class BaseModel(QtCore.QAbstractTableModel):

    def __init__(self, heads, datas):
        super().__init__()
        self.datas = datas
        self.originHeads = heads
        self.heads = list(filter(lambda x: 'hidden' not in x or not x['hidden'], heads))

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
                    if isinstance(item[key], int):
                        return str(int(item[key]))
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

    def icon_fun(self, key, item) -> QIcon:
        pass

    def date_time_fun(self, key, item) -> str:
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item[key] / 1000)) if item[key] else None
