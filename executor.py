import json
from typing import Callable

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QMessageBox
from httpx import Response

from request import Request


class HttpExecutor(object):
    def __init__(self):
        super().__init__()

    # 异步执行一个http请求线程
    def execute_http(self, thread_name: str, new_thread: QThread, result_call: Callable = None):
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
        QMessageBox.critical(None, '错误', err)


class HttpInterceptor(object):

    def handler(self, response):
        if response.status_code != 200:
            self.error.emit(f'请求远程服务器失败,错误代码{response.status_code}')
        else:
            result = json.loads(response.text)
            if not result['success']:
                self.error.emit(result['errMsg'])
            else:
                self.response.emit(result, response)


class PostThread(QThread, HttpInterceptor):
    response = Signal(object, Response)
    error = Signal(str)

    def __init__(self, url, data=None, json=None, **kwargs):
        super().__init__()
        self.url = url
        self.data = data
        self.json = json
        self.kwargs = kwargs;

    def run(self):
        # try:
        response = Request.post(self.url, data=self.data, json=self.json, **self.kwargs)
        self.handler(response)
        # except Exception as e:
        #     traceback.print_exc(e)
        #     self.error.emit(str(e))


class GetThread(QThread, HttpInterceptor):
    response = Signal(object, Response)
    error = Signal(str)

    def __init__(self, url, params=None, **kwargs):
        super().__init__()
        self.url = url
        self.params = params
        self.kwargs = kwargs;

    def run(self):
        # try:
        response = Request.get(self.url, params=self.params, **self.kwargs)
        self.handler(response)
        # except Exception as e:
        #     traceback.print_exc(e)
        #     self.error.emit(str(e))
