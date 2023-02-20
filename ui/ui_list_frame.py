# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_ListFrame(object):
    def setupUi(self, ListFrame):
        if not ListFrame.objectName():
            ListFrame.setObjectName(u"ListFrame")
        ListFrame.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ListFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(ListFrame)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(ListFrame)

        QMetaObject.connectSlotsByName(ListFrame)
    # setupUi

    def retranslateUi(self, ListFrame):
        ListFrame.setWindowTitle(QCoreApplication.translate("ListFrame", u"Form", None))
    # retranslateUi

