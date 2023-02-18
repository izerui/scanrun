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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import images_rc

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(979, 716)
        Home.setStyleSheet(u"QPushButton#evilButton {\n"
"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.action = QAction(Home)
        self.action.setObjectName(u"action")
        icon = QIcon(QIcon.fromTheme(u"applications-science"))
        self.action.setIcon(icon)
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, 12, -1, 12)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
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
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 1, 1, 1)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 30))
        self.pushButton_5.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))
        self.pushButton_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pageInput = QSpinBox(self.widget)
        self.pageInput.setObjectName(u"pageInput")
        self.pageInput.setMinimumSize(QSize(0, 30))
        self.pageInput.setMaximumSize(QSize(16777215, 30))
        self.pageInput.setMaximum(9999)
        self.pageInput.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.pageInput.setDisplayIntegerBase(10)

        self.horizontalLayout.addWidget(self.pageInput)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.widget, 1, 1, 1, 1, Qt.AlignLeft)


        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 42))
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/dengchu.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(160, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.widget_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/yj04.png", QSize(), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setPointSize(13)
        icon3 = QIcon()
        icon3.addFile(u":/logo/pic/scan.png", QSize(), QIcon.Normal, QIcon.On)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setFont(0, font);
        __qtreewidgetitem1.setIcon(0, icon2);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setIcon(0, icon3);
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setAutoExpandDelay(1)
        self.treeWidget.setExpandsOnDoubleClick(True)

        self.verticalLayout.addWidget(self.treeWidget)


        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 1)

        Home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 979, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        Home.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)

        self.retranslateUi(Home)
        self.menubar.triggered.connect(Home.toolbarClicked)
        self.pushButton.clicked.connect(Home.logout)
        self.pushButton_5.clicked.connect(Home.prePage)
        self.pushButton_6.clicked.connect(Home.nextPage)
        self.pushButton_3.clicked.connect(Home.endPage)
        self.pushButton_4.clicked.connect(Home.jumpPage)
        self.pushButton_2.clicked.connect(Home.firstPage)

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
        self.pushButton_2.setText(QCoreApplication.translate("Home", u"\u9996\u9875", None))
        self.pushButton_5.setText(QCoreApplication.translate("Home", u"\u4e0a\u4e00\u9875", None))
        self.pushButton_6.setText(QCoreApplication.translate("Home", u"\u4e0b\u4e00\u9875", None))
        self.pushButton_3.setText(QCoreApplication.translate("Home", u"\u5c3e\u9875", None))
        self.pushButton_4.setText(QCoreApplication.translate("Home", u"\u8df3\u8f6c\u5230", None))
        self.label.setText(QCoreApplication.translate("Home", u"--", None))
        self.pushButton.setText(QCoreApplication.translate("Home", u"\u6ce8\u9500", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Home", u"\u83dc\u5355", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Home", u"\u6211\u7684\u7ecf\u7ba1", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Home", u"\u626b\u7801\u4efb\u52a1", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.menu.setTitle(QCoreApplication.translate("Home", u"\u7cfb\u7edf", None))
    # retranslateUi

