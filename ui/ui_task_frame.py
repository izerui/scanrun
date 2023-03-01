# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_frame.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QTableView, QToolButton, QVBoxLayout, QWidget)
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
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(Qt.ClickFocus)
        icon = QIcon()
        icon.addFile(u":/logo/pic/search.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon)

        self.searchLayout.addWidget(self.pushButton, 0, 8, 1, 1, Qt.AlignLeft)

        self.label_03 = QLabel(self.verticalLayoutWidget)
        self.label_03.setObjectName(u"label_03")
        self.label_03.setMaximumSize(QSize(120, 16777215))
        self.label_03.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_03, 0, 4, 1, 1, Qt.AlignRight)

        self.CUSTOMER_MATERIAL = QLineEdit(self.verticalLayoutWidget)
        self.CUSTOMER_MATERIAL.setObjectName(u"CUSTOMER_MATERIAL")
        self.CUSTOMER_MATERIAL.setMinimumSize(QSize(0, 0))
        self.CUSTOMER_MATERIAL.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.CUSTOMER_MATERIAL, 0, 5, 1, 1)

        self.label_02 = QLabel(self.verticalLayoutWidget)
        self.label_02.setObjectName(u"label_02")
        self.label_02.setMaximumSize(QSize(120, 16777215))
        self.label_02.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_02, 0, 2, 1, 1, Qt.AlignRight)

        self.CUSTOMER_SERIAL = QLineEdit(self.verticalLayoutWidget)
        self.CUSTOMER_SERIAL.setObjectName(u"CUSTOMER_SERIAL")
        self.CUSTOMER_SERIAL.setMinimumSize(QSize(0, 0))
        self.CUSTOMER_SERIAL.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.CUSTOMER_SERIAL, 0, 7, 1, 1)

        self.label_04 = QLabel(self.verticalLayoutWidget)
        self.label_04.setObjectName(u"label_04")
        self.label_04.setMaximumSize(QSize(120, 16777215))
        self.label_04.setLayoutDirection(Qt.LeftToRight)

        self.searchLayout.addWidget(self.label_04, 0, 6, 1, 1, Qt.AlignRight)

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

        self.CUSTOMER_ORDER_DOC_NO = QLineEdit(self.verticalLayoutWidget)
        self.CUSTOMER_ORDER_DOC_NO.setObjectName(u"CUSTOMER_ORDER_DOC_NO")
        self.CUSTOMER_ORDER_DOC_NO.setMinimumSize(QSize(0, 0))
        self.CUSTOMER_ORDER_DOC_NO.setFocusPolicy(Qt.ClickFocus)

        self.searchLayout.addWidget(self.CUSTOMER_ORDER_DOC_NO, 0, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/reset.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon1)

        self.searchLayout.addWidget(self.pushButton_2, 0, 9, 1, 1)


        self.verticalLayout.addLayout(self.searchLayout)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFocusPolicy(Qt.StrongFocus)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableView)

        self.widget_2 = QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_6 = QFrame(self.widget_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_6)

        self.toolButton_7 = QToolButton(self.widget_2)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setMinimumSize(QSize(24, 24))
        self.toolButton_7.setMaximumSize(QSize(24, 24))
        self.toolButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_7.setFocusPolicy(Qt.ClickFocus)
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/first.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_7.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.toolButton_7)

        self.toolButton_8 = QToolButton(self.widget_2)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setMinimumSize(QSize(0, 24))
        self.toolButton_8.setMaximumSize(QSize(24, 24))
        self.toolButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_8.setFocusPolicy(Qt.ClickFocus)
        icon3 = QIcon()
        icon3.addFile(u":/logo/pic/pre.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_8.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.toolButton_8)

        self.toolButton_9 = QToolButton(self.widget_2)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setMinimumSize(QSize(0, 24))
        self.toolButton_9.setMaximumSize(QSize(24, 24))
        self.toolButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_9.setFocusPolicy(Qt.ClickFocus)
        icon4 = QIcon()
        icon4.addFile(u":/logo/pic/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_9.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.toolButton_9)

        self.toolButton_10 = QToolButton(self.widget_2)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setMinimumSize(QSize(0, 24))
        self.toolButton_10.setMaximumSize(QSize(24, 24))
        self.toolButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_10.setFocusPolicy(Qt.ClickFocus)
        icon5 = QIcon()
        icon5.addFile(u":/logo/pic/end.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_10.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.toolButton_10)

        self.line_5 = QFrame(self.widget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_5)

        self.toolButton_11 = QToolButton(self.widget_2)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setMinimumSize(QSize(0, 24))
        self.toolButton_11.setMaximumSize(QSize(24, 24))
        self.toolButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_11.setFocusPolicy(Qt.ClickFocus)
        icon6 = QIcon()
        icon6.addFile(u":/logo/pic/jump.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_11.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.toolButton_11)

        self.pageEdit = QSpinBox(self.widget_2)
        self.pageEdit.setObjectName(u"pageEdit")
        self.pageEdit.setMinimumSize(QSize(0, 24))
        self.pageEdit.setMaximumSize(QSize(16777215, 24))
        self.pageEdit.setFocusPolicy(Qt.ClickFocus)
        self.pageEdit.setMaximum(9999)
        self.pageEdit.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.pageEdit.setDisplayIntegerBase(10)

        self.horizontalLayout_2.addWidget(self.pageEdit)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.line_7 = QFrame(self.widget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_7)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(100, 32))
        font = QFont()
        font.setPointSize(11)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setFocusPolicy(Qt.ClickFocus)
        icon7 = QIcon()
        icon7.addFile(u":/logo/pic/scanIco.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_12.setIcon(icon7)
        self.pushButton_12.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.pushButton_12)

        self.line_8 = QFrame(self.widget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_8)


        self.verticalLayout.addWidget(self.widget_2)

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
        self.toolButton_8.clicked.connect(TaskFrame.prePage)
        self.toolButton_10.clicked.connect(TaskFrame.endPage)
        self.toolButton_9.clicked.connect(TaskFrame.nextPage)
        self.toolButton_11.clicked.connect(TaskFrame.jumpPage)
        self.toolButton_7.clicked.connect(TaskFrame.firstPage)
        self.pushButton_12.clicked.connect(TaskFrame.openTaskForm)
        self.ORDER_DOC_NO.textChanged.connect(TaskFrame.completerLineEdit)
        self.CUSTOMER_ORDER_DOC_NO.textChanged.connect(TaskFrame.completerLineEdit)
        self.CUSTOMER_MATERIAL.textChanged.connect(TaskFrame.completerLineEdit)
        self.CUSTOMER_SERIAL.textChanged.connect(TaskFrame.completerLineEdit)
        self.pushButton.clicked.connect(TaskFrame.firstPage)
        self.pushButton_2.clicked.connect(TaskFrame.resetEdits)

        QMetaObject.connectSlotsByName(TaskFrame)
    # setupUi

    def retranslateUi(self, TaskFrame):
        TaskFrame.setWindowTitle(QCoreApplication.translate("TaskFrame", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("TaskFrame", u"\u5f00\u59cb\u67e5\u8be2", None))
        self.label_03.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u6599\u53f7:", None))
        self.label_02.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u8ba2\u5355\u53f7:", None))
        self.label_04.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u7f16\u7801:", None))
        self.label_01.setText(QCoreApplication.translate("TaskFrame", u"\u9500\u552e\u5355\u53f7:", None))
        self.pushButton_2.setText(QCoreApplication.translate("TaskFrame", u"\u91cd\u7f6e\u67e5\u8be2", None))
        self.label_2.setText(QCoreApplication.translate("TaskFrame", u"--", None))
#if QT_CONFIG(tooltip)
        self.toolButton_7.setToolTip(QCoreApplication.translate("TaskFrame", u"\u9996\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_7.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_8.setToolTip(QCoreApplication.translate("TaskFrame", u"\u4e0a\u4e00\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_9.setToolTip(QCoreApplication.translate("TaskFrame", u"\u4e0b\u4e00\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_9.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_10.setToolTip(QCoreApplication.translate("TaskFrame", u"\u672b\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_10.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_11.setToolTip(QCoreApplication.translate("TaskFrame", u"\u8df3\u8f6c\u5230", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_11.setText("")
        self.label.setText(QCoreApplication.translate("TaskFrame", u"\u9875", None))
#if QT_CONFIG(tooltip)
        self.pushButton_12.setToolTip(QCoreApplication.translate("TaskFrame", u"\u8bf7\u9009\u62e9\u4e00\u6761\u8bb0\u5f55\u5e76\u5f00\u59cb\u626b\u63cf", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_12.setText(QCoreApplication.translate("TaskFrame", u"\u5f00\u59cb\u626b\u63cf", None))
    # retranslateUi

