import httpx
import asyncio
import nest_asyncio

nest_asyncio.apply()

class NetUtil(object):
    """
    请求代理工具类
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }

    loop = asyncio.get_event_loop()

    @classmethod
    def get(cls, url, params=None, callback=None, **exargs):
        if 'postCode' in exargs:
            cls.headers['postCode'] = exargs['postCode']
            del exargs['postCode']
        else:
            if 'postCode' in cls.headers:
                del cls.headers['postCode']
        exargs.setdefault("headers", cls.headers)
        exargs.setdefault('allow_redirects', True)
        if not callback:
            return httpx.get(url=url, params=params, **exargs);
        else:
            def wrapCall(res):
                result = res.result()
                callback(result)
            task = asyncio.ensure_future(httpx.AsyncClient().get(url=url, params=params, **exargs), loop=cls.loop)
            task.add_done_callback(callback)
            cls.loop.run_until_complete(task)
            return None


    @classmethod
    def post(cls, url, data=None, json=None, callback=None, **exargs):
        if 'postCode' in exargs:
            cls.headers['postCode'] = exargs['postCode']
            del exargs['postCode']
        else:
            if 'postCode' in cls.headers:
                del cls.headers['postCode']
        exargs.setdefault("headers", cls.headers)
        if not callback:
            return httpx.post(url, data=data, json=json, **exargs)
        else:
            def wrapCall(res):
                result = res.result()
                callback(result)
            task = asyncio.ensure_future(httpx.AsyncClient().post(url, data=data, json=json, **exargs), loop=cls.loop)
            task.add_done_callback(wrapCall)
            cls.loop.run_until_complete(task)
            return None

    @classmethod
    def setCookies(cls, value):
        cls.headers['cookie'] = value
