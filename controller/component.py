from typing import Callable

from PySide6.QtWidgets import QMessageBox


class ConfirmMessageBox(QMessageBox):

    def __init__(self, title, message):
        super().__init__()
        self.setIcon(QMessageBox.Icon.Question)
        self.setWindowTitle(title)
        self.setText(message)
        self.yes = self.addButton('确认', QMessageBox.ButtonRole.YesRole)
        self.yes.setFocus()
        self.no = self.addButton('取消', QMessageBox.ButtonRole.NoRole)
        self.setDefaultButton(self.yes)

    def show(self, success: Callable) -> int:
        exe = super().exec()
        if self.clickedButton() == self.yes:
            success()
        return exe
