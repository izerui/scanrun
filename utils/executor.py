# -*- coding: UTF-8 -*-
import json
import sys
from platform import system
from typing import Callable

import simpleaudio as sa
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QMessageBox
from httpx import Response

from utils.db import ScanTableUnit
from utils.request import Request


class ThreadExecutor(object):

    def __init__(self):
        super().__init__()

    def runAsync(self, thread_name: str, new_thread: QThread, callback: Callable = None):
        if hasattr(self, thread_name) and getattr(self, thread_name).isRunning():
            pass
        else:
            setattr(self, thread_name, new_thread)
            if callback:
                getattr(getattr(self, thread_name), 'callback').connect(callback)
            getattr(self, thread_name).start()


class HttpExecutor(object):
    def __init__(self):
        super().__init__()

    # 异步执行一个http请求线程
    def http(self, thread_name: str, new_thread: QThread, result_call: Callable = None):
        if hasattr(self, thread_name) and getattr(self, thread_name).isRunning():
            pass
        else:
            setattr(self, thread_name, new_thread)
            if result_call:
                getattr(getattr(self, thread_name), 'response').connect(result_call)
            getattr(getattr(self, thread_name), 'error').connect(self.http_error_call)
            getattr(self, thread_name).start()

    # 默认的异常回调
    def http_error_call(self, err):
        QMessageBox.critical(None, '错误', err['errMsg'])
        # if err['errCode'] == 'unLogin':
        #     sys.exit()


class HttpInterceptor(object):

    def handler(self, response):
        if response.status_code != 200:
            self.error.emit({
                'errCode': f'REQUEST_ERROR_{response.status_code}',
                'errMsg': f'请求远程服务器失败,错误代码{response.status_code}'
            })
        else:
            result = json.loads(response.text)
            if not result['success']:
                self.error.emit({
                    'errCode': result['errCode'],
                    'errMsg': result['errMsg']
                })
            else:
                self.response.emit(result, response)


class PostThread(QThread, HttpInterceptor):
    response = Signal(object, Response)
    error = Signal(dict)

    def __init__(self, url, data=None, json=None, **kwargs):
        super().__init__()
        self.url = url
        self.data = data
        self.json = json
        self.kwargs = kwargs;

    def run(self):
        try:
            response = Request.post(self.url, data=self.data, json=self.json, **self.kwargs)
        except Exception as e:
            raise e;
        self.handler(response)
        # except Exception as e:
        #     traceback.print_exc(e)
        #     self.error.emit(str(e))


class GetThread(QThread, HttpInterceptor):
    response = Signal(object, Response)
    error = Signal(dict)

    def __init__(self, url, params=None, **kwargs):
        super().__init__()
        self.url = url
        self.params = params
        self.kwargs = kwargs;

    def run(self):
        try:
            response = Request.get(self.url, params=self.params, **self.kwargs)
        except Exception as e:
            raise e;
        self.handler(response)
        # except Exception as e:
        #     traceback.print_exc(e)
        #     self.error.emit(str(e))


#
# class SqlExecutor(object):
#     def __init__(self):
#         super().__init__()
#
#     # 异步执行一个sql查询
#     def execute(self, thread_name: str, new_thread: QThread, result_call: Callable = None):
#         if hasattr(self, thread_name) and getattr(self, thread_name).isRunning():
#             pass
#         else:
#             setattr(self, thread_name, new_thread)
#             if result_call:
#                 getattr(getattr(self, thread_name), 'response').connect(result_call)
#             getattr(getattr(self, thread_name), 'error').connect(self.http_error_call)
#             getattr(self, thread_name).start()
#
#
# class SqlThread(QThread):
#     result = Signal(QSqlQuery)
#
#     def __init__(self, sql, dict=None):
#         super().__init__()
#         self.sql = sql
#         self.dict = dict
#
#     def run(self) -> None:
#         query = DbUnit.execute(self.sql, self.dict)
#         self.result.emit(query)

class SoundThread(QThread):

    def __init__(self, file):
        super().__init__()
        self.filePath = f'{sys.path[0]}{file}'
        # self.filePathName = os.path.splitext(self.filePath)[0]
        # self.fileExt = os.path.splitext(self.filePath)[-1]
        self.system = system()

    def run(self) -> None:
        try:
            wave_obj = sa.WaveObject.from_wave_file(self.filePath)
            play_obj = wave_obj.play()
            # play_obj.wait_done()
        except:
            pass


class AsyncScanedDataLoader(QThread):
    result = Signal(int, int, list)

    def __init__(self, scanTableUnit: ScanTableUnit):
        super().__init__()
        self.scanTableUnit = scanTableUnit
        self.stopStatus = False

    def run(self) -> None:
        start = 0
        count = 1000
        while True:
            if self.stopStatus:
                break
            datas = self.scanTableUnit.queryForList(
                f'SELECT * FROM {self.scanTableUnit.tableName} where complete = 1 order by create_time desc limit {start},{count}')
            size = len(datas)
            self.result.emit(start, size, datas)
            start += size
            if not datas:
                break

    def stop_wait(self):
        self.stopStatus = True
        while self.isRunning():
            self.quit()
            pass
        print(self.isRunning())

    def stop_no_wait(self):
        self.stopStatus = True
