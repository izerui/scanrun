# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan_frame.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLCDNumber, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QWidget)
import images_rc

class Ui_ScanFrame(object):
    def setupUi(self, ScanFrame):
        if not ScanFrame.objectName():
            ScanFrame.setObjectName(u"ScanFrame")
        ScanFrame.resize(744, 538)
        ScanFrame.setAutoFillBackground(False)
        ScanFrame.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(ScanFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(ScanFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"backgrond-color: rgb(170, 121, 66)")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_3 = QLCDNumber(self.groupBox_2)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setMinimumSize(QSize(0, 32))
        self.lcdNumber_3.setStyleSheet(u"")
        self.lcdNumber_3.setFrameShape(QFrame.Box)
        self.lcdNumber_3.setFrameShadow(QFrame.Raised)
        self.lcdNumber_3.setMode(QLCDNumber.Dec)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_8.addWidget(self.lcdNumber_3, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_2 = QLCDNumber(self.groupBox_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setMinimumSize(QSize(0, 32))
        self.lcdNumber_2.setStyleSheet(u"")
        self.lcdNumber_2.setFrameShape(QFrame.Box)
        self.lcdNumber_2.setFrameShadow(QFrame.Raised)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setMode(QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdNumber_2, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(0, 32))
        self.lcdNumber.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(24)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setStyleSheet(u"")
        self.lcdNumber.setFrameShape(QFrame.Box)
        self.lcdNumber.setFrameShadow(QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 111.000000000000000)

        self.gridLayout_6.addWidget(self.lcdNumber, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 1, 1, 2)


        self.gridLayout_3.addWidget(self.frame, 1, 2, 1, 1)

        self.frame_2 = QFrame(ScanFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(-1)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(13)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/logo/pic/return_home.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)

        self.chejian_name_input = QLineEdit(self.frame_2)
        self.chejian_name_input.setObjectName(u"chejian_name_input")
        self.chejian_name_input.setMaximumSize(QSize(16777215, 24))
        self.chejian_name_input.setFocusPolicy(Qt.NoFocus)
        self.chejian_name_input.setReadOnly(True)

        self.gridLayout.addWidget(self.chejian_name_input, 2, 1, 1, 1)

        self.order_no_input = QLineEdit(self.frame_2)
        self.order_no_input.setObjectName(u"order_no_input")
        self.order_no_input.setMaximumSize(QSize(16777215, 24))
        self.order_no_input.setTabletTracking(False)
        self.order_no_input.setFocusPolicy(Qt.NoFocus)
        self.order_no_input.setReadOnly(True)

        self.gridLayout.addWidget(self.order_no_input, 1, 1, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.prompt_label = QLabel(self.frame_2)
        self.prompt_label.setObjectName(u"prompt_label")
        font2 = QFont()
        font2.setPointSize(24)
        self.prompt_label.setFont(font2)

        self.gridLayout.addWidget(self.prompt_label, 4, 3, 1, 1)

        self.cus_order_no_input = QLineEdit(self.frame_2)
        self.cus_order_no_input.setObjectName(u"cus_order_no_input")
        self.cus_order_no_input.setMaximumSize(QSize(16777215, 24))
        self.cus_order_no_input.setFocusPolicy(Qt.NoFocus)
        self.cus_order_no_input.setReadOnly(True)

        self.gridLayout.addWidget(self.cus_order_no_input, 1, 3, 1, 1)

        self.scan_code_input = QLineEdit(self.frame_2)
        self.scan_code_input.setObjectName(u"scan_code_input")
        self.scan_code_input.setMinimumSize(QSize(0, 0))
        self.scan_code_input.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(28)
        self.scan_code_input.setFont(font3)
        self.scan_code_input.setMouseTracking(True)
        self.scan_code_input.setFocusPolicy(Qt.StrongFocus)
        self.scan_code_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.scan_code_input, 4, 1, 1, 2)

        self.banzu_name_input = QLineEdit(self.frame_2)
        self.banzu_name_input.setObjectName(u"banzu_name_input")
        self.banzu_name_input.setFocusPolicy(Qt.NoFocus)
        self.banzu_name_input.setReadOnly(True)

        self.gridLayout.addWidget(self.banzu_name_input, 2, 3, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.user_name_input = QLineEdit(self.frame_2)
        self.user_name_input.setObjectName(u"user_name_input")
        self.user_name_input.setFocusPolicy(Qt.NoFocus)
        self.user_name_input.setReadOnly(True)

        self.gridLayout.addWidget(self.user_name_input, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)

        self.task_count_input = QLineEdit(self.frame_2)
        self.task_count_input.setObjectName(u"task_count_input")
        self.task_count_input.setFocusPolicy(Qt.NoFocus)
        self.task_count_input.setReadOnly(True)

        self.gridLayout.addWidget(self.task_count_input, 3, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 2)

        self.tableWidget = QTableWidget(ScanFrame)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFocusPolicy(Qt.ClickFocus)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_3.addWidget(self.tableWidget, 2, 0, 1, 3)

        self.widget = QWidget(ScanFrame)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/delete.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon1)

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 3, 0, 1, 3)

#if QT_CONFIG(shortcut)
        self.label_6.setBuddy(self.banzu_name_input)
        self.label_7.setBuddy(self.cus_order_no_input)
        self.label_2.setBuddy(self.scan_code_input)
        self.label_4.setBuddy(self.order_no_input)
        self.label_3.setBuddy(self.chejian_name_input)
        self.label_8.setBuddy(self.user_name_input)
        self.label_5.setBuddy(self.task_count_input)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scan_code_input, self.chejian_name_input)
        QWidget.setTabOrder(self.chejian_name_input, self.order_no_input)
        QWidget.setTabOrder(self.order_no_input, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.cus_order_no_input)

        self.retranslateUi(ScanFrame)
        self.pushButton.clicked.connect(ScanFrame.returnHome)
        self.scan_code_input.returnPressed.connect(ScanFrame.scan)
        self.pushButton_2.clicked.connect(ScanFrame.deleteSelection)

        QMetaObject.connectSlotsByName(ScanFrame)
    # setupUi

    def retranslateUi(self, ScanFrame):
        ScanFrame.setWindowTitle(QCoreApplication.translate("ScanFrame", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u5361\u677f\u6570\u91cf", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u7bb1\u5b50\u6570\u91cf", None))
        self.groupBox.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u4ea7\u54c1\u6570\u91cf", None))
        self.pushButton.setText(QCoreApplication.translate("ScanFrame", u"\u8fd4\u56de", None))
        self.label_6.setText(QCoreApplication.translate("ScanFrame", u"\u73ed\u7ec4\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("ScanFrame", u"\u5ba2\u6237\u5355\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("ScanFrame", u"\u626b\u7801\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("ScanFrame", u"\u8ba2\u5355\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("ScanFrame", u"\u8f66\u95f4\uff1a", None))
        self.prompt_label.setText(QCoreApplication.translate("ScanFrame", u"\u4ea7\u54c1", None))
        self.scan_code_input.setText(QCoreApplication.translate("ScanFrame", u"32423643", None))
        self.label_8.setText(QCoreApplication.translate("ScanFrame", u"\u64cd\u4f5c\u5458\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("ScanFrame", u"\u4efb\u52a1\u6570\u91cf\uff1a", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ScanFrame", u"\u8f66\u95f4", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ScanFrame", u"\u73ed\u7ec4", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ScanFrame", u"\u626b\u7801\u65f6\u95f4", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ScanFrame", u"\u64cd\u4f5c\u4eba", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ScanFrame", u"\u4ea7\u54c1\u7801", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ScanFrame", u"\u7bb1\u7801", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ScanFrame", u"\u5361\u677f\u7801", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ScanFrame", u"\u4e0a\u4f20\u72b6\u6001", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ScanFrame", u"\u4e0a\u4f20\u4eba", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ScanFrame", u"\u4e0a\u4f20\u65f6\u95f4", None));
        self.pushButton_2.setText(QCoreApplication.translate("ScanFrame", u"\u5220\u9664", None))
    # retranslateUi

