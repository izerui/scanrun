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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLCDNumber, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QWidget)
import images_rc

class Ui_ScanFrame(object):
    def setupUi(self, ScanFrame):
        if not ScanFrame.objectName():
            ScanFrame.setObjectName(u"ScanFrame")
        ScanFrame.resize(744, 538)
        ScanFrame.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(ScanFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(ScanFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_2 = QLCDNumber(self.groupBox_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setMinimumSize(QSize(0, 32))
        self.lcdNumber_2.setFrameShape(QFrame.Box)
        self.lcdNumber_2.setFrameShadow(QFrame.Raised)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setMode(QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdNumber_2, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_3 = QLCDNumber(self.groupBox_2)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setMinimumSize(QSize(0, 32))
        self.lcdNumber_3.setFrameShape(QFrame.Box)
        self.lcdNumber_3.setFrameShadow(QFrame.Raised)
        self.lcdNumber_3.setMode(QLCDNumber.Dec)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_8.addWidget(self.lcdNumber_3, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
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


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lineEdit_5 = QLineEdit(ScanFrame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.lineEdit_5, 1, 3, 1, 1)

        self.lineEdit_3 = QLineEdit(ScanFrame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 3)

        self.label_2 = QLabel(ScanFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(ScanFrame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.label_4 = QLabel(ScanFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(ScanFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(ScanFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 3)

        self.label_3 = QLabel(ScanFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButton = QPushButton(ScanFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 34))
        self.pushButton.setMaximumSize(QSize(16777215, 34))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/logo/pic/return_home.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 3)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget = QTableWidget(ScanFrame)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_4.addWidget(self.tableWidget, 0, 1, 1, 1)

        self.treeWidget = QTreeWidget(ScanFrame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout_4.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(ScanFrame)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_4.addWidget(self.tableWidget_2, 0, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 2, 0, 1, 2)


        self.retranslateUi(ScanFrame)
        self.pushButton.clicked.connect(ScanFrame.returnHome)

        QMetaObject.connectSlotsByName(ScanFrame)
    # setupUi

    def retranslateUi(self, ScanFrame):
        ScanFrame.setWindowTitle(QCoreApplication.translate("ScanFrame", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u7bb1\u5b50\u6570\u91cf", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u5361\u677f\u6570\u91cf", None))
        self.groupBox.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u4ea7\u54c1\u6570\u91cf", None))
        self.label_2.setText(QCoreApplication.translate("ScanFrame", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("ScanFrame", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("ScanFrame", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("ScanFrame", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("ScanFrame", u"\u8fd4\u56de", None))
    # retranslateUi

