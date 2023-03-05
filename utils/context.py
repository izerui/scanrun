# -*- coding: UTF-8 -*-
import asyncio
import os
import sys
from typing import Any, Tuple

import librosa
from PySide6.QtCore import QSettings

import simpleaudio as sa
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

    # errorSound: Tuple = librosa.load(f'{mediaPath}error.wav')
    # unitSound: Tuple = librosa.load(f'{mediaPath}unit.wav')
    # boxSound: Tuple = librosa.load(f'{mediaPath}box.wav')
    # palletSound: Tuple = librosa.load(f'{mediaPath}pallet.wav')

    errorSound: WaveObject = sa.WaveObject.from_wave_file(f'{mediaPath}error.wav')
    unitSound: WaveObject = sa.WaveObject.from_wave_file(f'{mediaPath}unit.wav')
    boxSound: WaveObject = sa.WaveObject.from_wave_file(f'{mediaPath}box.wav')
    palletSound: WaveObject = sa.WaveObject.from_wave_file(f'{mediaPath}pallet.wav')
    # loop = asyncio.get_event_loop()
    # @staticmethod
    # async def playError():
    #     asyncio.run_coroutine_threadsafe(Context.errorSound.play(), Context.loop)
    #
    # @staticmethod
    # async def playUnit():
    #     asyncio.run_coroutine_threadsafe(Context.unitSound.play(), Context.loop)
    #
    # @staticmethod
    # async def playBox():
    #     asyncio.run_coroutine_threadsafe(Context.boxSound.play(), Context.loop)
    #
    # @staticmethod
    # async def playPallet():
    #     asyncio.run_coroutine_threadsafe(Context.palletSound.play(), Context.loop)

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
