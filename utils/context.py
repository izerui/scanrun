# -*- coding: UTF-8 -*-
import os
import sys
from typing import Any

import simpleaudio as sa
from PySide6.QtCore import QSettings
from simpleaudio import WaveObject


class User:
    __slots__ = ['entCode', 'entName', 'userCode', 'userName']

    def __init__(self, entCode: str, entName: str, userCode: str, userName: str):
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

    rootPath = f'{sys.path[0]}{os.sep}'
    mediaPath = f'{rootPath}media{os.sep}'

    errorSound: WaveObject = sa.WaveObject.from_wave_file(f'{mediaPath}error.wav')
    unitSound: WaveObject = sa.WaveObject.from_wave_file(f'{mediaPath}unit.wav')
    boxSound: WaveObject = sa.WaveObject.from_wave_file(f'{mediaPath}box.wav')
    palletSound: WaveObject = sa.WaveObject.from_wave_file(f'{mediaPath}pallet.wav')

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
