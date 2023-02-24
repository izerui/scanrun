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
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
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
        self.tabWidget = QTabWidget(ScanFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tab0 = QWidget()
        self.tab0.setObjectName(u"tab0")
        self.verticalLayout = QVBoxLayout(self.tab0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table0 = QTableWidget(self.tab0)
        if (self.table0.columnCount() < 7):
            self.table0.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table0.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table0.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table0.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table0.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table0.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table0.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table0.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table0.setObjectName(u"table0")
        self.table0.setFocusPolicy(Qt.ClickFocus)
        self.table0.setAlternatingRowColors(True)
        self.table0.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table0.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table0.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.table0)

        self.widget = QWidget(self.tab0)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        icon = QIcon()
        icon.addFile(u":/logo/pic/delete.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon)

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.tabWidget.addTab(self.tab0, "")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.gridLayout_9 = QGridLayout(self.tab1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.table1 = QTableWidget(self.tab1)
        if (self.table1.columnCount() < 10):
            self.table1.setColumnCount(10)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table1.setHorizontalHeaderItem(9, __qtablewidgetitem16)
        self.table1.setObjectName(u"table1")

        self.gridLayout_9.addWidget(self.table1, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab1, "")

        self.gridLayout_3.addWidget(self.tabWidget, 2, 0, 1, 3)

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
        font = QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/return_home.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.scan_code_input = QLineEdit(self.frame_2)
        self.scan_code_input.setObjectName(u"scan_code_input")
        self.scan_code_input.setMinimumSize(QSize(0, 0))
        self.scan_code_input.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(28)
        self.scan_code_input.setFont(font1)
        self.scan_code_input.setMouseTracking(True)
        self.scan_code_input.setFocusPolicy(Qt.StrongFocus)
        self.scan_code_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.scan_code_input, 5, 1, 1, 2)

        self.chejian_name_input = QLineEdit(self.frame_2)
        self.chejian_name_input.setObjectName(u"chejian_name_input")
        self.chejian_name_input.setMaximumSize(QSize(16777215, 24))
        self.chejian_name_input.setFocusPolicy(Qt.NoFocus)
        self.chejian_name_input.setReadOnly(True)

        self.gridLayout.addWidget(self.chejian_name_input, 3, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)

        self.task_count_input = QLineEdit(self.frame_2)
        self.task_count_input.setObjectName(u"task_count_input")
        self.task_count_input.setFocusPolicy(Qt.NoFocus)
        self.task_count_input.setReadOnly(True)

        self.gridLayout.addWidget(self.task_count_input, 4, 3, 1, 1)

        self.order_no_input = QLineEdit(self.frame_2)
        self.order_no_input.setObjectName(u"order_no_input")
        self.order_no_input.setMaximumSize(QSize(16777215, 24))
        self.order_no_input.setTabletTracking(False)
        self.order_no_input.setFocusPolicy(Qt.NoFocus)
        self.order_no_input.setReadOnly(True)

        self.gridLayout.addWidget(self.order_no_input, 1, 1, 1, 1)

        self.user_name_input = QLineEdit(self.frame_2)
        self.user_name_input.setObjectName(u"user_name_input")
        self.user_name_input.setFocusPolicy(Qt.NoFocus)
        self.user_name_input.setReadOnly(True)

        self.gridLayout.addWidget(self.user_name_input, 4, 1, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.cus_order_no_input = QLineEdit(self.frame_2)
        self.cus_order_no_input.setObjectName(u"cus_order_no_input")
        self.cus_order_no_input.setMaximumSize(QSize(16777215, 24))
        self.cus_order_no_input.setFocusPolicy(Qt.NoFocus)
        self.cus_order_no_input.setReadOnly(True)

        self.gridLayout.addWidget(self.cus_order_no_input, 1, 3, 1, 1)

        self.prompt_label = QLabel(self.frame_2)
        self.prompt_label.setObjectName(u"prompt_label")
        font2 = QFont()
        font2.setPointSize(24)
        self.prompt_label.setFont(font2)

        self.gridLayout.addWidget(self.prompt_label, 5, 3, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.inventory_code_input = QLineEdit(self.frame_2)
        self.inventory_code_input.setObjectName(u"inventory_code_input")
        self.inventory_code_input.setFocusPolicy(Qt.NoFocus)
        self.inventory_code_input.setReadOnly(True)

        self.gridLayout.addWidget(self.inventory_code_input, 2, 1, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)

        self.banzu_name_input = QLineEdit(self.frame_2)
        self.banzu_name_input.setObjectName(u"banzu_name_input")
        self.banzu_name_input.setFocusPolicy(Qt.NoFocus)
        self.banzu_name_input.setReadOnly(True)

        self.gridLayout.addWidget(self.banzu_name_input, 3, 3, 1, 1)

        self.inventory_name_input = QLineEdit(self.frame_2)
        self.inventory_name_input.setObjectName(u"inventory_name_input")
        self.inventory_name_input.setFocusPolicy(Qt.NoFocus)
        self.inventory_name_input.setReadOnly(True)

        self.gridLayout.addWidget(self.inventory_name_input, 2, 3, 1, 1)

        self.unit_rule_label = QLabel(self.frame_2)
        self.unit_rule_label.setObjectName(u"unit_rule_label")
        font3 = QFont()
        font3.setFamilies([u".AppleSystemUIFont"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.unit_rule_label.setFont(font3)
        self.unit_rule_label.setCursor(QCursor(Qt.IBeamCursor))
        self.unit_rule_label.setStyleSheet(u"color: rgb(255, 38, 0);")

        self.gridLayout.addWidget(self.unit_rule_label, 0, 2, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 2)

        self.frame = QFrame(ScanFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font4 = QFont()
        font4.setPointSize(18)
        self.groupBox_2.setFont(font4)
        self.groupBox_2.setStyleSheet(u"backgrond-color: rgb(170, 121, 66)")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lcd_pallet = QLCDNumber(self.groupBox_2)
        self.lcd_pallet.setObjectName(u"lcd_pallet")
        self.lcd_pallet.setMinimumSize(QSize(0, 32))
        self.lcd_pallet.setStyleSheet(u"")
        self.lcd_pallet.setFrameShape(QFrame.Box)
        self.lcd_pallet.setFrameShadow(QFrame.Raised)
        self.lcd_pallet.setMode(QLCDNumber.Dec)
        self.lcd_pallet.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_8.addWidget(self.lcd_pallet, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font4)
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lcd_box = QLCDNumber(self.groupBox_3)
        self.lcd_box.setObjectName(u"lcd_box")
        self.lcd_box.setMinimumSize(QSize(0, 32))
        self.lcd_box.setStyleSheet(u"")
        self.lcd_box.setFrameShape(QFrame.Box)
        self.lcd_box.setFrameShadow(QFrame.Raised)
        self.lcd_box.setSmallDecimalPoint(False)
        self.lcd_box.setMode(QLCDNumber.Dec)
        self.lcd_box.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcd_box, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font4)
        self.groupBox.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lcd_unit = QLCDNumber(self.groupBox)
        self.lcd_unit.setObjectName(u"lcd_unit")
        self.lcd_unit.setMinimumSize(QSize(0, 32))
        self.lcd_unit.setSizeIncrement(QSize(0, 0))
        font5 = QFont()
        font5.setFamilies([u"Academy Engraved LET"])
        font5.setPointSize(24)
        font5.setBold(True)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.lcd_unit.setFont(font5)
        self.lcd_unit.setAutoFillBackground(False)
        self.lcd_unit.setStyleSheet(u"")
        self.lcd_unit.setFrameShape(QFrame.Box)
        self.lcd_unit.setFrameShadow(QFrame.Raised)
        self.lcd_unit.setSmallDecimalPoint(False)
        self.lcd_unit.setMode(QLCDNumber.Dec)
        self.lcd_unit.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_unit.setProperty("value", 111.000000000000000)

        self.gridLayout_6.addWidget(self.lcd_unit, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 1, 1, 2)


        self.gridLayout_3.addWidget(self.frame, 1, 2, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.chejian_name_input)
        self.label_5.setBuddy(self.task_count_input)
        self.label_8.setBuddy(self.user_name_input)
        self.label_4.setBuddy(self.order_no_input)
        self.label_7.setBuddy(self.cus_order_no_input)
        self.label_6.setBuddy(self.banzu_name_input)
        self.label_2.setBuddy(self.scan_code_input)
        self.label.setBuddy(self.inventory_code_input)
        self.label_9.setBuddy(self.inventory_name_input)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scan_code_input, self.table1)

        self.retranslateUi(ScanFrame)
        self.pushButton.clicked.connect(ScanFrame.returnHome)
        self.scan_code_input.returnPressed.connect(ScanFrame.scan)
        self.pushButton_2.clicked.connect(ScanFrame.deleteSelection)
        self.tabWidget.currentChanged.connect(ScanFrame.tabChanged)
        self.table0.itemClicked.connect(ScanFrame.unUploadDataSelected)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ScanFrame)
    # setupUi

    def retranslateUi(self, ScanFrame):
        ScanFrame.setWindowTitle(QCoreApplication.translate("ScanFrame", u"Form", None))
        ___qtablewidgetitem = self.table0.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ScanFrame", u"\u8f66\u95f4", None));
        ___qtablewidgetitem1 = self.table0.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ScanFrame", u"\u73ed\u7ec4", None));
        ___qtablewidgetitem2 = self.table0.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ScanFrame", u"\u64cd\u4f5c\u4eba", None));
        ___qtablewidgetitem3 = self.table0.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ScanFrame", u"\u626b\u7801\u65f6\u95f4", None));
        ___qtablewidgetitem4 = self.table0.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ScanFrame", u"\u4ea7\u54c1\u7801", None));
        ___qtablewidgetitem5 = self.table0.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ScanFrame", u"\u7bb1\u7801", None));
        ___qtablewidgetitem6 = self.table0.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ScanFrame", u"\u5361\u677f\u7801", None));
        self.pushButton_2.setText(QCoreApplication.translate("ScanFrame", u"\u5220\u9664", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab0), QCoreApplication.translate("ScanFrame", u"\u672a\u5305\u88c5", None))
        ___qtablewidgetitem7 = self.table1.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ScanFrame", u"\u8f66\u95f4", None));
        ___qtablewidgetitem8 = self.table1.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ScanFrame", u"\u73ed\u7ec4", None));
        ___qtablewidgetitem9 = self.table1.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ScanFrame", u"\u64cd\u4f5c\u4eba", None));
        ___qtablewidgetitem10 = self.table1.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ScanFrame", u"\u626b\u7801\u65f6\u95f4", None));
        ___qtablewidgetitem11 = self.table1.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ScanFrame", u"\u4ea7\u54c1\u7801", None));
        ___qtablewidgetitem12 = self.table1.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ScanFrame", u"\u7bb1\u7801", None));
        ___qtablewidgetitem13 = self.table1.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ScanFrame", u"\u5361\u677f\u7801", None));
        ___qtablewidgetitem14 = self.table1.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ScanFrame", u"\u4e0a\u4f20\u72b6\u6001", None));
        ___qtablewidgetitem15 = self.table1.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ScanFrame", u"\u4e0a\u4f20\u4eba", None));
        ___qtablewidgetitem16 = self.table1.horizontalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ScanFrame", u"\u4e0a\u4f20\u65f6\u95f4", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("ScanFrame", u"\u5df2\u5305\u88c5", None))
        self.pushButton.setText(QCoreApplication.translate("ScanFrame", u"\u8fd4\u56de", None))
        self.scan_code_input.setText("")
        self.label_3.setText(QCoreApplication.translate("ScanFrame", u"\u8f66\u95f4\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("ScanFrame", u"\u4efb\u52a1\u6570\u91cf\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("ScanFrame", u"\u64cd\u4f5c\u5458\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("ScanFrame", u"\u8ba2\u5355\u53f7\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("ScanFrame", u"\u5ba2\u6237\u5355\u53f7\uff1a", None))
        self.prompt_label.setText(QCoreApplication.translate("ScanFrame", u"\u4ea7\u54c1", None))
        self.label_6.setText(QCoreApplication.translate("ScanFrame", u"\u73ed\u7ec4\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("ScanFrame", u"\u626b\u7801\uff1a", None))
        self.label.setText(QCoreApplication.translate("ScanFrame", u"\u6210\u54c1\u7f16\u7801\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("ScanFrame", u"\u6210\u54c1\u540d\u79f0\uff1a", None))
        self.unit_rule_label.setText(QCoreApplication.translate("ScanFrame", u"--", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u5361\u677f\u6570\u91cf", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u7bb1\u5b50\u6570\u91cf", None))
        self.groupBox.setTitle(QCoreApplication.translate("ScanFrame", u"\u5df2\u626b\u63cf\u4ea7\u54c1\u6570\u91cf", None))
    # retranslateUi

