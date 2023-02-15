from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from ui.ui_home import Ui_Home_Form


class HomeWindow(QWidget):
    loginExistSignal = Signal(str)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home_Form()
        self.ui.setupUi(self)
