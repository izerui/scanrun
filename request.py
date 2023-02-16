from PySide6.QtCore import QThread, Signal

import httpx


class Request(object):
    """
    请求代理工具类
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }

    @classmethod
    def get(cls, url, params=None, **kwargs):
        if 'postCode' in kwargs:
            cls.headers['postCode'] = kwargs['postCode']
            del kwargs['postCode']
        else:
            if 'postCode' in cls.headers:
                del cls.headers['postCode']
        kwargs.setdefault("headers", cls.headers)
        kwargs.setdefault('allow_redirects', True)
        return httpx.get(url=url, params=params, **kwargs);

    @classmethod
    def post(cls, url, data=None, json=None, **kwargs):
        if 'postCode' in kwargs:
            cls.headers['postCode'] = kwargs['postCode']
            del kwargs['postCode']
        else:
            if 'postCode' in cls.headers:
                del cls.headers['postCode']
        kwargs.setdefault("headers", cls.headers)
        return httpx.post(url, data=data, json=json, **kwargs)

    @classmethod
    async def getAsync(cls, url, params=None, **kwargs):
        if 'postCode' in kwargs:
            cls.headers['postCode'] = kwargs['postCode']
            del kwargs['postCode']
        else:
            if 'postCode' in cls.headers:
                del cls.headers['postCode']
        kwargs.setdefault("headers", cls.headers)
        kwargs.setdefault('allow_redirects', True)
        async with httpx.AsyncClient() as client:
            resp = await client.get(url=url, params=params, **kwargs)
            return resp

    @classmethod
    async def postAsync(cls, url, data=None, json=None, **kwargs):
        if 'postCode' in kwargs:
            cls.headers['postCode'] = kwargs['postCode']
            del kwargs['postCode']
        else:
            if 'postCode' in cls.headers:
                del cls.headers['postCode']
        kwargs.setdefault("headers", cls.headers)
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, data=data, json=json, **kwargs)
            return resp

    @classmethod
    def setCookies(cls, value):
        cls.headers['cookie'] = value


class PostThread(QThread):
    resultSignal = Signal(object)

    def __init__(self, url, data=None, json=None, **kwargs):
        super().__init__()
        self.url = url
        self.data = data
        self.json = json
        self.kwargs = kwargs;

    def run(self):
        result = Request.post(self.url, data=self.data, json=self.json, **self.kwargs)
        self.resultSignal.emit(result)


class GetThread(QThread):
    resultSignal = Signal(object)

    def __init__(self, url, params=None, **kwargs):
        super().__init__()
        self.url = url
        self.params = params
        self.kwargs = kwargs;

    def run(self):
        result = Request.get(self.url, params=self.params, **self.kwargs)
        self.resultSignal.emit(result)
