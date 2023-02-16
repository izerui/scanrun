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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QToolBar, QWidget)
import images_rc

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(979, 716)
        self.action = QAction(Home)
        self.action.setObjectName(u"action")
        icon = QIcon()
        iconThemeName = u"applications-science"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../images_rc/pic/login.png", QSize(), QIcon.Normal, QIcon.Off)

        self.action.setIcon(icon)
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 60))
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(840, 10, 91, 41))
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/logout.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon1)
        self.line = QFrame(self.groupBox_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(780, 10, 3, 61))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 441, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 41))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 41))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 41))

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)

        Home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 979, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        Home.setMenuBar(self.menubar)
        self.toolBar = QToolBar(Home)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMinimumSize(QSize(0, 41))
        Home.addToolBar(Qt.BottomToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.toolBar.addAction(self.action)

        self.retranslateUi(Home)
        self.menubar.triggered.connect(Home.toolbarClicked)
        self.pushButton.clicked.connect(Home.logout)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("Home", u"\u5173\u4e8e", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Home", u"\u9500\u552e\u5355\u53f7", u"\u65b9\u6cd5"));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Home", u"\u5ba2\u6237\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Home", u"\u5ba2\u6237\u8ba2\u5355\u53f7", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Home", u"\u8ba2\u5355\u91d1\u989d", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Home", u"\u4e1a\u52a1\u5458", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Home", u"\u521b\u5efa\u65f6\u95f4", None));
        self.groupBox_3.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("Home", u"\u9000\u51fa\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Home", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Home", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Home", u"PushButton", None))
        self.menu.setTitle(QCoreApplication.translate("Home", u"\u7cfb\u7edf", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Home", u"toolBar", None))
    # retranslateUi

