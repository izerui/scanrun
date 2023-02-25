from PySide6.QtWidgets import QWidget

from ui.ui_list_frame import Ui_ListFrame
from utils.executor import HttpExecutor


class ListFrame(QWidget, Ui_ListFrame, HttpExecutor):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
