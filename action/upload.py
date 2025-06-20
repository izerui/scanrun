import time

from PySide6.QtWidgets import QMessageBox, QProgressBar

from model import ScanModel
from utils.context import Context
from utils.db import ScanTableUnit
from utils.executor import PostThread, HttpExecutor


class UploadAction(HttpExecutor):

    def __init__(self, model: ScanModel, orderInfo: dict, scanTableUnit: ScanTableUnit, progressBar: QProgressBar):
        super().__init__()
        self.model = model
        self.orderInfo = orderInfo
        self.scanTableUnit = scanTableUnit
        self.progressBar = progressBar
        self.origin_progressBar_value = progressBar.value()
        self.origin_progressBar_max_value = progressBar.maximum()

    def start(self):
        # 全部待上传的列表，所有未上传的数据
        self.upload_total_items = list(filter(lambda x: x['upload_status'] == 0, self.model.datas))
        if not self.upload_total_items:
            QMessageBox.information(None, '提示', '无待上传数据')
            return
        self.progressBar.setMaximum(len(self.upload_total_items))
        # 当前正在上传的分片列表
        self.upload_current_items = []
        # 当前正在上传的起始索引
        self.upload_current_index = 0
        # 当前已经上传完毕的数量
        self.upload_current_finished_count = 0
        # 开始分片上传
        self.uploadFragment()

    # 分片上传
    def uploadFragment(self):
        self.upload_current_items = self.upload_total_items[self.upload_current_index:self.upload_current_index + 200]
        if not self.upload_current_items:
            if self.upload_current_finished_count == len(self.upload_total_items):
                QMessageBox.information(None, '成功', '上传完毕')
            self.complete()
            return
        uploadRequest = {
            'entCode': Context.user.entCode,
            'businessKey': self.orderInfo["saleInventoryRecordId"],
            'data': []
        }
        for item in self.upload_current_items:
            item['upload_status'] = 1
            item['uploader'] = Context.user.userCode
            item['uploader_name'] = Context.user.userName
            item['upload_time'] = int(round(time.time() * 1000))
            uploadRequest['data'].append({
                'chejianCode': item['chejian_code'],
                'chejianName': item['chejian_name'],
                'banzuCode': item['banzu_code'],
                'banzuName': item['banzu_name'],
                'creator': item['creator'],
                'creatorName': item['creator_name'],
                'createTime': item['create_time'],
                'unitCode': item['unit_code'],
                'boxCode': item['box_code'],
                'palletCode': item['pallet_code'],
                'uploader': item['uploader'],
                'uploaderName': item['uploader_name'],
                'uploadTime': item['upload_time']
            })
            self.upload_current_finished_count += 1

        self.progressBar.setValue(self.upload_current_finished_count)
        self.http('uploadThread',
                  PostThread(f'{Context.getSettings("gateway/domain")}/sale-pc/v1/scan/code/record/insert',
                             json=uploadRequest), self.continueUploadFragment)

    # 每个分片上传成功后修改状态并继续下一个分片
    def continueUploadFragment(self, result, response):
        self.scanTableUnit.updateBatch(self.upload_current_items)
        self.upload_current_index += 200
        self.uploadFragment()

    def complete(self):
        self.progressBar.setMaximum(self.origin_progressBar_max_value)
        self.progressBar.setValue(self.origin_progressBar_value)
