# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QGridLayout, QGroupBox, QSplitter, QTableWidget)

class Ui_ListFrame(object):
    def setupUi(self, ListFrame):
        if not ListFrame.objectName():
            ListFrame.setObjectName(u"ListFrame")
        ListFrame.resize(724, 557)
        self.gridLayout_3 = QGridLayout(ListFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter = QSplitter(ListFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, -1)
        self.tableWidget_2 = QTableWidget(self.groupBox_2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_2.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_2)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(ListFrame)

        QMetaObject.connectSlotsByName(ListFrame)
    # setupUi

    def retranslateUi(self, ListFrame):
        ListFrame.setWindowTitle(QCoreApplication.translate("ListFrame", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("ListFrame", u"\u4efb\u52a1\u5217\u8868", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ListFrame", u"\u626b\u63cf\u6570\u636e", None))
    # retranslateUi

