import requests

class FkRequest(object):
    """
    请求代理工具类
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }

    @classmethod
    def request(cls, method, url, **kwargs):
        kwargs.setdefault("headers", cls.headers)
        response = requests.request(method, url, **kwargs)
        response.encoding = response.apparent_encoding
        return response

    @classmethod
    def get(cls, url, params=None, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return cls.request('get', url, params=params, **kwargs)

    @classmethod
    def post(cls, url, data=None, json=None, **kwargs):
        return cls.request('post', url, data=data, json=json, **kwargs)

    @classmethod
    def setCookies(cls, value):
        cls.headers['cookie'] = value