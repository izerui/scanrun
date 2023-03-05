# -*- coding: UTF-8 -*-
import json

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
        # kwargs.setdefault('allow_redirects', True)
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

    @staticmethod
    def getError(response):
        if response.status_code != 200:
            return {
                'errCode': f'REQUEST_ERROR_{response.status_code}',
                'errMsg': f'请求远程服务器失败,错误代码{response.status_code}'
            }
        else:
            result = json.loads(response.text)
            if not result['success']:
                return {
                    'errCode': result['errCode'],
                    'errMsg': result['errMsg']
                }
            else:
                return None

    @classmethod
    def setCookies(cls, value):
        cls.headers['cookie'] = value
