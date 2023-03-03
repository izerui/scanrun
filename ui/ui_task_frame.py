# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_frame.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from controller.component import PagingWidget

import images_rc

class Ui_TaskFrame(object):
    def setupUi(self, TaskFrame):
        if not TaskFrame.objectName():
            TaskFrame.setObjectName(u"TaskFrame")
        TaskFrame.resize(931, 682)
        TaskFrame.setStyleSheet(u"")
        self.gridLayout = QGridLayout(TaskFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(TaskFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setEnabled(True)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(True)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.searchLayout = QGridLayout()
        self.searchLayout.setObjectName(u"searchLayout")
        self.CUSTOMER_SERIAL = QLineEdit(self.verticalLayoutWidget)
        self.CUSTOMER_SERIAL.setObjectName(u"CUSTOMER_SERIAL")
        self.CUSTOMER_SERIAL.setMinimumSize(QSize(0, 0))
        self.CUSTOMER_SERIAL.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.CUSTOMER_SERIAL, 0, 7, 1, 1)

        self.CUSTOMER_MATERIAL = QLineEdit(self.verticalLayoutWidget)
        self.CUSTOMER_MATERIAL.setObjectName(u"CUSTOMER_MATERIAL")
        self.CUSTOMER_MATERIAL.setMinimumSize(QSize(0, 0))
        self.CUSTOMER_MATERIAL.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.CUSTOMER_MATERIAL, 0, 5, 1, 1)

        self.label_01 = QLabel(self.verticalLayoutWidget)
        self.label_01.setObjectName(u"label_01")
        self.label_01.setMaximumSize(QSize(120, 16777215))
        self.label_01.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_01, 0, 0, 1, 1, Qt.AlignRight)

        self.ORDER_DOC_NO = QLineEdit(self.verticalLayoutWidget)
        self.ORDER_DOC_NO.setObjectName(u"ORDER_DOC_NO")
        self.ORDER_DOC_NO.setMinimumSize(QSize(0, 0))
        self.ORDER_DOC_NO.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.ORDER_DOC_NO, 0, 1, 1, 1)

        self.label_04 = QLabel(self.verticalLayoutWidget)
        self.label_04.setObjectName(u"label_04")
        self.label_04.setMaximumSize(QSize(120, 16777215))
        self.label_04.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_04, 0, 6, 1, 1, Qt.AlignRight)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setFocusPolicy(Qt.ClickFocus)
        icon = QIcon()
        icon.addFile(u":/logo/pic/scanIco.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QSize(16, 16))

        self.searchLayout.addWidget(self.pushButton_12, 0, 10, 1, 1)

        self.label_03 = QLabel(self.verticalLayoutWidget)
        self.label_03.setObjectName(u"label_03")
        self.label_03.setMaximumSize(QSize(120, 16777215))
        self.label_03.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_03, 0, 4, 1, 1, Qt.AlignRight)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(Qt.ClickFocus)
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/search.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon1)

        self.searchLayout.addWidget(self.pushButton, 0, 8, 1, 1, Qt.AlignLeft)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/reset.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon2)

        self.searchLayout.addWidget(self.pushButton_2, 0, 9, 1, 1)

        self.CUSTOMER_ORDER_DOC_NO = QLineEdit(self.verticalLayoutWidget)
        self.CUSTOMER_ORDER_DOC_NO.setObjectName(u"CUSTOMER_ORDER_DOC_NO")
        self.CUSTOMER_ORDER_DOC_NO.setMinimumSize(QSize(0, 0))
        self.CUSTOMER_ORDER_DOC_NO.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.CUSTOMER_ORDER_DOC_NO, 0, 3, 1, 1)

        self.label_02 = QLabel(self.verticalLayoutWidget)
        self.label_02.setObjectName(u"label_02")
        self.label_02.setMaximumSize(QSize(120, 16777215))
        self.label_02.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_02, 0, 2, 1, 1, Qt.AlignRight)


        self.verticalLayout.addLayout(self.searchLayout)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFocusPolicy(Qt.StrongFocus)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableView)

        self.paging = PagingWidget(self.verticalLayoutWidget)
        self.paging.setObjectName(u"paging")
        self.paging.setMinimumSize(QSize(0, 12))

        self.verticalLayout.addWidget(self.paging)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setFocusPolicy(Qt.ClickFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 905, 69))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_3.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_3.setHorizontalSpacing(3)
        self.formLayout_3.setVerticalSpacing(-1)

        self.verticalLayout_2.addLayout(self.formLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(TaskFrame)
        self.ORDER_DOC_NO.textChanged.connect(TaskFrame.completerLineEdit)
        self.CUSTOMER_ORDER_DOC_NO.textChanged.connect(TaskFrame.completerLineEdit)
        self.CUSTOMER_MATERIAL.textChanged.connect(TaskFrame.completerLineEdit)
        self.CUSTOMER_SERIAL.textChanged.connect(TaskFrame.completerLineEdit)
        self.pushButton_2.clicked.connect(TaskFrame.resetEdits)
        self.pushButton_12.clicked.connect(TaskFrame.openTaskForm)
        self.pushButton.clicked.connect(TaskFrame.firstPage)

        QMetaObject.connectSlotsByName(TaskFrame)
    # setupUi

    def retranslateUi(self, TaskFrame):
        TaskFrame.setWindowTitle(QCoreApplication.translate("TaskFrame", u"Form", None))
        self.label_01.setText(QCoreApplication.translate("TaskFrame", u"\u9500\u552e\u5355\u53f7:", None))
        self.label_04.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u7f16\u7801:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_12.setToolTip(QCoreApplication.translate("TaskFrame", u"\u8bf7\u9009\u62e9\u4e00\u6761\u8bb0\u5f55\u5e76\u5f00\u59cb\u626b\u63cf", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_12.setText(QCoreApplication.translate("TaskFrame", u"\u5f00\u59cb\u626b\u63cf", None))
        self.label_03.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u6599\u53f7:", None))
        self.pushButton.setText(QCoreApplication.translate("TaskFrame", u"\u67e5\u8be2", None))
        self.pushButton_2.setText(QCoreApplication.translate("TaskFrame", u"\u91cd\u7f6e", None))
        self.label_02.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u8ba2\u5355\u53f7:", None))
    # retranslateUi

