import httpx
import asyncio

class NetUtil(object):
    """
    请求代理工具类
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }

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
            task = asyncio.ensure_future(httpx.AsyncClient().get(url=url, params=params, **exargs))
            task.add_done_callback(callback)
            asyncio.get_event_loop().run_until_complete(task)
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
            task = asyncio.ensure_future(httpx.AsyncClient().post(url, data=data, json=json, **exargs))
            task.add_done_callback(wrapCall)
            asyncio.get_event_loop().run_until_complete(task)
            return None

    @classmethod
    async def getAsync(cls, url, params=None, **exargs):
        if 'postCode' in exargs:
            cls.headers['postCode'] = exargs['postCode']
            del exargs['postCode']
        else:
            if 'postCode' in cls.headers:
                del cls.headers['postCode']
        exargs.setdefault("headers", cls.headers)
        exargs.setdefault('allow_redirects', True)
        async with httpx.AsyncClient() as client:
            resp = await client.get(url=url, params=params, **exargs)
            return resp

    @classmethod
    async def postAsync(cls, url, data=None, json=None, **exargs):
        if 'postCode' in exargs:
            cls.headers['postCode'] = exargs['postCode']
            del exargs['postCode']
        else:
            if 'postCode' in cls.headers:
                del cls.headers['postCode']
        exargs.setdefault("headers", cls.headers)
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, data=data, json=json, **exargs)
            return resp

    @classmethod
    def setCookies(cls, value):
        cls.headers['cookie'] = value
