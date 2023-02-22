from PySide6.QtCore import QSettings


class Context(object):
    """
    全局上下文
    """

    user: dict = None

    settings: QSettings = QSettings('settings.ini', QSettings.IniFormat)
    settings.setFallbacksEnabled(False)

    @staticmethod
    def setDefaultSettings(key, value):
        v = Context.settings.value(key)
        if not v:
            Context.settings.setValue(key, value)
    @staticmethod
    def getSettings(key) -> None:
        return Context.settings.value(key)

    @staticmethod
    def setSettings(key, value):
        Context.settings.setValue(key, value)