# -*- coding: UTF-8 -*-
import json
import logging
import sys
from platform import system
from threading import Thread
from typing import Callable

import librosa
import simpleaudio
import simpleaudio as sa
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QMessageBox
from httpx import Response
from simpleaudio import WaveObject

from utils.db import ScanTableUnit
from utils.request import Request


class ThreadExecutor(object):

    def __init__(self):
        super().__init__()


    def runAsync(self, thread_name: str, new_thread: QThread, callback: Callable = None):
        if hasattr(self, thread_name) and getattr(self, thread_name).isRunning():
            logging.warn(f'{thread_name} 正在运行...')
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
    def http(self, thread_name: str, new_thread: QThread, response: Callable = None, error: Callable = lambda err: QMessageBox.critical(None, '错误', err['errMsg'])):
        if hasattr(self, thread_name) and getattr(self, thread_name).isRunning():
            logging.warn(f'{thread_name} 正在运行...')
            pass
        else:
            setattr(self, thread_name, new_thread)
            if response:
                getattr(getattr(self, thread_name), 'response').connect(response)
            getattr(getattr(self, thread_name), 'error').connect(error)
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
            logging.exception(e)
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
            logging.exception(e)
            raise e;
        self.handler(response)
        # except Exception as e:
        #     traceback.print_exc(e)
        #     self.error.emit(str(e))

class SoundThread(QThread):

    def __init__(self, sound:WaveObject):
        super().__init__()
        self.sound = sound
        # self.filePathName = os.path.splitext(self.filePath)[0]
        # self.fileExt = os.path.splitext(self.filePath)[-1]
        # self.system = system()

    def run(self) -> None:
        try:
            self.sound.play()
            self.wait_done()
        except:
            pass
