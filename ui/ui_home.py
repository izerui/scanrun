# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

from controller.list import ListFrame
from controller.scan import ScanFrame
from controller.task import TaskFrame
import images_rc

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(1054, 712)
        Home.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/logo/pic/logo.png", QSize(), QIcon.Normal, QIcon.On)
        Home.setWindowIcon(icon)
        Home.setStyleSheet(u"")
        Home.setUnifiedTitleAndToolBarOnMac(False)
        self.homeAction = QAction(Home)
        self.homeAction.setObjectName(u"homeAction")
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/return_home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeAction.setIcon(icon1)
        self.scanAction = QAction(Home)
        self.scanAction.setObjectName(u"scanAction")
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/scanIco.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/logo/pic/scanIco1.png", QSize(), QIcon.Active, QIcon.On)
        icon2.addFile(u":/logo/pic/scanIco1.png", QSize(), QIcon.Selected, QIcon.On)
        self.scanAction.setIcon(icon2)
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, 12, -1, 12)
        self.leftFrame = QFrame(self.centralwidget)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMinimumSize(QSize(120, 0))
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_task = QPushButton(self.leftFrame)
        self.tabButtonGroup = QButtonGroup(Home)
        self.tabButtonGroup.setObjectName(u"tabButtonGroup")
        self.tabButtonGroup.addButton(self.btn_task)
        self.btn_task.setObjectName(u"btn_task")
        self.btn_task.setMinimumSize(QSize(0, 42))
        font = QFont()
        font.setPointSize(12)
        self.btn_task.setFont(font)
        self.btn_task.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/logo/pic/scanIco1.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_task.setIcon(icon3)
        self.btn_task.setCheckable(True)
        self.btn_task.setChecked(True)
        self.btn_task.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btn_task)

        self.btn_data = QPushButton(self.leftFrame)
        self.tabButtonGroup.addButton(self.btn_data)
        self.btn_data.setObjectName(u"btn_data")
        self.btn_data.setMinimumSize(QSize(0, 42))
        self.btn_data.setFont(font)
        self.btn_data.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/logo/pic/data.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_data.setIcon(icon4)
        self.btn_data.setCheckable(True)
        self.btn_data.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.btn_data)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.leftFrame, 0, 0, 1, 1)

        self.stackedTab = QStackedWidget(self.centralwidget)
        self.stackedTab.setObjectName(u"stackedTab")
        self.stackedTab.setAutoFillBackground(False)
        self.stackedTab.setFrameShape(QFrame.StyledPanel)
        self.taskFrame = TaskFrame()
        self.taskFrame.setObjectName(u"taskFrame")
        self.verticalLayout_2 = QVBoxLayout(self.taskFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.stackedTab.addWidget(self.taskFrame)
        self.listFrame = ListFrame()
        self.listFrame.setObjectName(u"listFrame")
        self.stackedTab.addWidget(self.listFrame)
        self.scanFrame = ScanFrame()
        self.scanFrame.setObjectName(u"scanFrame")
        self.stackedTab.addWidget(self.scanFrame)

        self.gridLayout.addWidget(self.stackedTab, 0, 1, 1, 1)

        Home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1054, 24))
        Home.setMenuBar(self.menubar)

        self.retranslateUi(Home)
        self.tabButtonGroup.buttonClicked.connect(Home.tabButtonPressed)

        self.stackedTab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"SN\u5e8f\u5217\u53f7\u626b\u7801\u88c5\u7bb1\u7cfb\u7edf", None))
        self.homeAction.setText(QCoreApplication.translate("Home", u"home", None))
        self.scanAction.setText(QCoreApplication.translate("Home", u"scan", None))
#if QT_CONFIG(tooltip)
        self.scanAction.setToolTip(QCoreApplication.translate("Home", u"\u5f00\u59cb\u626b\u7801", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_task.setToolTip(QCoreApplication.translate("Home", u"\u663e\u793a\u4efb\u52a1\u5217\u8868,\u5e76\u51c6\u5907\u5f00\u59cb\u626b\u7801", None))
#endif // QT_CONFIG(tooltip)
        self.btn_task.setText(QCoreApplication.translate("Home", u"\u626b\u63cf\u4efb\u52a1", None))
#if QT_CONFIG(tooltip)
        self.btn_data.setToolTip(QCoreApplication.translate("Home", u"\u663e\u793a\u5df2\u626b\u63cf\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
        self.btn_data.setText(QCoreApplication.translate("Home", u"\u5df2\u626b\u6570\u636e", None))
    # retranslateUi

