# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from controller.component import PagingWidget
from controller.component import DateRange

import images_rc

class Ui_RecordFrame(object):
    def setupUi(self, RecordFrame):
        if not RecordFrame.objectName():
            RecordFrame.setObjectName(u"RecordFrame")
        RecordFrame.resize(931, 682)
        RecordFrame.setStyleSheet(u"")
        self.gridLayout = QGridLayout(RecordFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(RecordFrame)
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
        self.searchLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.CUSTOMER_SERIAL = QLineEdit(self.verticalLayoutWidget)
        self.CUSTOMER_SERIAL.setObjectName(u"CUSTOMER_SERIAL")
        self.CUSTOMER_SERIAL.setMinimumSize(QSize(0, 0))
        self.CUSTOMER_SERIAL.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.CUSTOMER_SERIAL, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        icon = QIcon()
        icon.addFile(u":/logo/pic/reset.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon)

        self.searchLayout.addWidget(self.pushButton_2, 1, 6, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.searchLayout.addWidget(self.label, 1, 2, 1, 1, Qt.AlignRight)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.searchLayout.addWidget(self.label_4, 2, 2, 1, 1, Qt.AlignRight)

        self.label_03 = QLabel(self.verticalLayoutWidget)
        self.label_03.setObjectName(u"label_03")
        self.label_03.setMaximumSize(QSize(120, 16777215))
        self.label_03.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_03, 0, 4, 1, 1, Qt.AlignRight)

        self.label_04 = QLabel(self.verticalLayoutWidget)
        self.label_04.setObjectName(u"label_04")
        self.label_04.setMaximumSize(QSize(120, 16777215))
        self.label_04.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_04, 1, 0, 1, 1, Qt.AlignRight)

        self.CUSTOMER_MATERIAL = QLineEdit(self.verticalLayoutWidget)
        self.CUSTOMER_MATERIAL.setObjectName(u"CUSTOMER_MATERIAL")
        self.CUSTOMER_MATERIAL.setMinimumSize(QSize(0, 0))
        self.CUSTOMER_MATERIAL.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.CUSTOMER_MATERIAL, 0, 5, 1, 1)

        self.ORDER_DOC_NO = QLineEdit(self.verticalLayoutWidget)
        self.ORDER_DOC_NO.setObjectName(u"ORDER_DOC_NO")
        self.ORDER_DOC_NO.setMinimumSize(QSize(0, 0))
        self.ORDER_DOC_NO.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.ORDER_DOC_NO, 0, 1, 1, 1)

        self.BOX_CODE = QLineEdit(self.verticalLayoutWidget)
        self.BOX_CODE.setObjectName(u"BOX_CODE")
        self.BOX_CODE.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.BOX_CODE, 1, 5, 1, 1)

        self.PALLET_CODE = QLineEdit(self.verticalLayoutWidget)
        self.PALLET_CODE.setObjectName(u"PALLET_CODE")
        self.PALLET_CODE.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.PALLET_CODE, 2, 1, 1, 1)

        self.dateRange = DateRange(self.verticalLayoutWidget)
        self.dateRange.setObjectName(u"dateRange")
        self.dateRange.setMaximumSize(QSize(300, 16777215))
        self.dateRange.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.dateRange, 2, 3, 1, 3)

        self.UNIT_CODE = QLineEdit(self.verticalLayoutWidget)
        self.UNIT_CODE.setObjectName(u"UNIT_CODE")
        self.UNIT_CODE.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.UNIT_CODE, 1, 3, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.searchLayout.addWidget(self.label_3, 2, 0, 1, 1)

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

        self.label_01 = QLabel(self.verticalLayoutWidget)
        self.label_01.setObjectName(u"label_01")
        self.label_01.setMaximumSize(QSize(120, 16777215))
        self.label_01.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_01, 0, 0, 1, 1, Qt.AlignRight)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.searchLayout.addWidget(self.label_2, 1, 4, 1, 1, Qt.AlignRight)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(Qt.ClickFocus)
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/search.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon1)

        self.searchLayout.addWidget(self.pushButton, 0, 6, 1, 1)


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
        self.horizontalLayout_2 = QHBoxLayout(self.paging)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

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


        self.retranslateUi(RecordFrame)
        self.pushButton_2.clicked.connect(RecordFrame.resetEdits)
        self.CUSTOMER_MATERIAL.textChanged.connect(RecordFrame.completerLineEdit)
        self.CUSTOMER_ORDER_DOC_NO.textChanged.connect(RecordFrame.completerLineEdit)
        self.pushButton.clicked.connect(RecordFrame.firstPage)
        self.CUSTOMER_SERIAL.textChanged.connect(RecordFrame.completerLineEdit)
        self.PALLET_CODE.textChanged.connect(RecordFrame.completerLineEdit)
        self.BOX_CODE.textChanged.connect(RecordFrame.completerLineEdit)
        self.ORDER_DOC_NO.textChanged.connect(RecordFrame.completerLineEdit)
        self.UNIT_CODE.textChanged.connect(RecordFrame.completerLineEdit)
        self.ORDER_DOC_NO.returnPressed.connect(RecordFrame.firstPage)
        self.CUSTOMER_ORDER_DOC_NO.returnPressed.connect(RecordFrame.firstPage)
        self.CUSTOMER_MATERIAL.returnPressed.connect(RecordFrame.firstPage)
        self.CUSTOMER_SERIAL.returnPressed.connect(RecordFrame.firstPage)
        self.UNIT_CODE.returnPressed.connect(RecordFrame.firstPage)
        self.BOX_CODE.returnPressed.connect(RecordFrame.firstPage)
        self.PALLET_CODE.returnPressed.connect(RecordFrame.firstPage)

        QMetaObject.connectSlotsByName(RecordFrame)
    # setupUi

    def retranslateUi(self, RecordFrame):
        RecordFrame.setWindowTitle(QCoreApplication.translate("RecordFrame", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("RecordFrame", u"\u91cd\u7f6e\u67e5\u8be2", None))
        self.label.setText(QCoreApplication.translate("RecordFrame", u"\u4ea7\u54c1\u7801:", None))
        self.label_4.setText(QCoreApplication.translate("RecordFrame", u"\u65e5\u671f:", None))
        self.label_03.setText(QCoreApplication.translate("RecordFrame", u"\u5ba2\u6237\u6599\u53f7:", None))
        self.label_04.setText(QCoreApplication.translate("RecordFrame", u"\u5ba2\u6237\u7f16\u7801:", None))
        self.label_3.setText(QCoreApplication.translate("RecordFrame", u"\u5361\u677f\u7801:", None))
        self.label_02.setText(QCoreApplication.translate("RecordFrame", u"\u5ba2\u6237\u8ba2\u5355\u53f7:", None))
        self.label_01.setText(QCoreApplication.translate("RecordFrame", u"\u9500\u552e\u5355\u53f7:", None))
        self.label_2.setText(QCoreApplication.translate("RecordFrame", u"\u7bb1\u7801:", None))
        self.pushButton.setText(QCoreApplication.translate("RecordFrame", u"\u5f00\u59cb\u67e5\u8be2", None))
    # retranslateUi

