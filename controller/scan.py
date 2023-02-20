from PySide6.QtWidgets import QWidget

from executor import HttpExecutor
from ui.ui_scan_frame import Ui_ScanFrame


class ScanFrame(QWidget, Ui_ScanFrame, HttpExecutor):

    def __init__(self):
        super().__init__()
        self.setupUi(self)