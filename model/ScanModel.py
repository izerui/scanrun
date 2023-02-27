from PySide6 import QtGui
from PySide6.QtGui import QIcon

from model.BaseModel import BaseModel


class ScanModel(BaseModel):

    def __init__(self, type: int, datas):
        _heads = [
            {'title': '车间', 'code': 'chejian_name'},
            {'title': '班组', 'code': 'banzu_name'},
            {'title': '操作人', 'code': 'creator_name'},
            {'title': '扫码时间', 'code': 'create_time', 'label_format_fun': self.date_time_fun},
            {'title': '产品码', 'code': 'unit_code'},
            {'title': '箱玛', 'code': 'box_code'},
            {'title': '卡板码', 'code': 'pallet_code'},
            {'title': '上传状态', 'code': 'upload_status', 'hidden': type == 0, 'label_hidden': True,
             'icon_fun': self.icon_fun},
            {'title': '上传人', 'code': 'uploader', 'hidden': type == 0},
            {'title': '上传时间', 'code': 'upload_time', 'hidden': type == 0, 'label_format_fun': self.date_time_fun}
        ]
        super().__init__(_heads, datas)

    def icon_fun(self, key, item) -> QIcon:
        if key == 'upload_status':
            return QtGui.QIcon(':/logo/pic/yes.png') if item[key] and item[key] == 1 else QtGui.QIcon(
                ':/logo/pic/no.png')
