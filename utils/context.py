# -*- coding: UTF-8 -*-
from typing import Any

from PySide6.QtCore import QSettings


class User:
    __slots__ = ['entCode', 'entName', 'userCode', 'userName']

    def __init__(self, entCode:str, entName:str, userCode:str, userName:str):
        super().__init__()
        self.entCode = entCode
        self.entName = entName
        self.userCode = userCode
        self.userName = userName

class Context(object):
    """
    全局上下文
    """

    user: User = None

    settings: QSettings = QSettings('settings.ini', QSettings.IniFormat)
    settings.setFallbacksEnabled(False)

    @staticmethod
    def setDefaultSettings(key, value):
        v = Context.settings.value(key)
        if not v:
            Context.settings.setValue(key, value)

    @staticmethod
    def getSettings(key, default_value=None) -> Any:
        value = Context.settings.value(key)
        if not value:
            return default_value
        else:
            return value

    @staticmethod
    def setSettings(key, value):
        Context.settings.setValue(key, value)
