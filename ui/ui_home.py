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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableWidget, QTableWidgetItem, QToolBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
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
        self.actionlogout = QAction(Home)
        self.actionlogout.setObjectName(u"actionlogout")
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/logout2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionlogout.setIcon(icon1)
        self.actionscan = QAction(Home)
        self.actionscan.setObjectName(u"actionscan")
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/scanIco.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/logo/pic/scanIco1.png", QSize(), QIcon.Active, QIcon.On)
        icon2.addFile(u":/logo/pic/scanIco1.png", QSize(), QIcon.Selected, QIcon.On)
        self.actionscan.setIcon(icon2)
        self.action_2 = QAction(Home)
        self.action_2.setObjectName(u"action_2")
        icon3 = QIcon()
        icon3.addFile(u":/logo/pic/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_2.setIcon(icon3)
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(12, 12, -1, 12)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.gridLayout_3 = QGridLayout(self.page_13)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.page_13)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
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
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(24, 24))
        self.pushButton_2.setMaximumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u":/logo/pic/first.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon4)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 30))
        self.pushButton_5.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u":/logo/pic/pre.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_5.setIcon(icon5)

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u":/logo/pic/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_6.setIcon(icon6)

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/logo/pic/end.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_3.setIcon(icon7)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))
        self.pushButton_4.setMaximumSize(QSize(32, 32))
        icon8 = QIcon()
        icon8.addFile(u":/logo/pic/jump.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_4.setIcon(icon8)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pageInput = QSpinBox(self.widget)
        self.pageInput.setObjectName(u"pageInput")
        self.pageInput.setMinimumSize(QSize(0, 30))
        self.pageInput.setMaximumSize(QSize(16777215, 30))
        self.pageInput.setMaximum(9999)
        self.pageInput.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.pageInput.setDisplayIntegerBase(10)

        self.horizontalLayout.addWidget(self.pageInput)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 40))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/logo/pic/scanIco.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.widget)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 200))
        self.scrollArea.setMaximumSize(QSize(16777215, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 728, 202))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setHorizontalSpacing(3)
        self.Label = QLabel(self.scrollAreaWidgetContents)
        self.Label.setObjectName(u"Label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.Label)

        self.LineEdit_1 = QLineEdit(self.scrollAreaWidgetContents)
        self.LineEdit_1.setObjectName(u"LineEdit_1")
        self.LineEdit_1.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.LineEdit_1)

        self.Label2 = QLabel(self.scrollAreaWidgetContents)
        self.Label2.setObjectName(u"Label2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.Label2)

        self.Label3 = QLabel(self.scrollAreaWidgetContents)
        self.Label3.setObjectName(u"Label3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.Label3)

        self.LineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.LineEdit_3.setObjectName(u"LineEdit_3")
        self.LineEdit_3.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.LineEdit_3)

        self.Label54 = QLabel(self.scrollAreaWidgetContents)
        self.Label54.setObjectName(u"Label54")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.Label54)

        self.LineEdit_4 = QLineEdit(self.scrollAreaWidgetContents)
        self.LineEdit_4.setObjectName(u"LineEdit_4")
        self.LineEdit_4.setReadOnly(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.LineEdit_4)

        self.Label8 = QLabel(self.scrollAreaWidgetContents)
        self.Label8.setObjectName(u"Label8")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.Label8)

        self.LineEdit_5 = QLineEdit(self.scrollAreaWidgetContents)
        self.LineEdit_5.setObjectName(u"LineEdit_5")
        self.LineEdit_5.setReadOnly(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.LineEdit_5)

        self.LineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.LineEdit_2.setObjectName(u"LineEdit_2")
        self.LineEdit_2.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.LineEdit_2)

        self.Label_2 = QLabel(self.scrollAreaWidgetContents)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.Label_2)

        self.LineEdit_6 = QLineEdit(self.scrollAreaWidgetContents)
        self.LineEdit_6.setObjectName(u"LineEdit_6")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.LineEdit_6)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.gridLayout_3.addWidget(self.groupBox, 0, 1, 1, 1)

        self.widget_2 = QWidget(self.page_13)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(160, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.treeWidget = QTreeWidget(self.widget_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        icon10 = QIcon()
        icon10.addFile(u":/logo/pic/yj04.png", QSize(), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setPointSize(13)
        icon11 = QIcon()
        icon11.addFile(u":/logo/pic/scan.png", QSize(), QIcon.Normal, QIcon.On)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setFont(0, font);
        __qtreewidgetitem1.setIcon(0, icon10);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setIcon(0, icon11);
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setAutoExpandDelay(1)
        self.treeWidget.setExpandsOnDoubleClick(True)

        self.verticalLayout.addWidget(self.treeWidget)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.label_2 = QLabel(self.page_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 240, 58, 16))
        self.stackedWidget.addWidget(self.page_14)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        Home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 979, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        Home.setMenuBar(self.menubar)
        self.toolBar = QToolBar(Home)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBar.setFocusPolicy(Qt.ClickFocus)
        Home.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.toolBar.addAction(self.action_2)
        self.toolBar.addAction(self.actionlogout)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionscan)

        self.retranslateUi(Home)
        self.pushButton_4.clicked.connect(Home.jumpPage)
        self.pushButton_2.clicked.connect(Home.firstPage)
        self.pushButton_3.clicked.connect(Home.endPage)
        self.pushButton_5.clicked.connect(Home.prePage)
        self.pushButton_6.clicked.connect(Home.nextPage)
        self.tableWidget.itemSelectionChanged.connect(Home.dataRowSelected)
        self.pushButton.clicked.connect(Home.startScanJob)
        self.toolBar.actionTriggered.connect(Home.toolbarClicked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("Home", u"about", None))
        self.actionlogout.setText(QCoreApplication.translate("Home", u"logout", None))
#if QT_CONFIG(tooltip)
        self.actionlogout.setToolTip(QCoreApplication.translate("Home", u"\u8fd4\u56de\u767b\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.actionscan.setText(QCoreApplication.translate("Home", u"scan", None))
#if QT_CONFIG(tooltip)
        self.actionscan.setToolTip(QCoreApplication.translate("Home", u"\u5f00\u59cb\u626b\u7801", None))
#endif // QT_CONFIG(tooltip)
        self.action_2.setText(QCoreApplication.translate("Home", u"home", None))
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
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Home", u"\u9996\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("Home", u"\u4e0a\u4e00\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("Home", u"\u4e0b\u4e00\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("Home", u"\u672b\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("Home", u"\u8df3\u8f6c\u5230", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText("")
        self.label.setText(QCoreApplication.translate("Home", u"--", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Home", u"\u8bf7\u9009\u62e9\u4e00\u6761\u8bb0\u5f55\u5e76\u5f00\u59cb\u626b\u63cf", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Home", u"\u5f00\u59cb\u626b\u63cf", None))
        self.Label.setText(QCoreApplication.translate("Home", u"\u9500\u552e\u5355\u53f7", None))
        self.LineEdit_1.setText("")
        self.Label2.setText(QCoreApplication.translate("Home", u"\u5ba2\u6237\u540d\u79f0", None))
        self.Label3.setText(QCoreApplication.translate("Home", u"\u5ba2\u6237\u8ba2\u5355\u53f7", None))
        self.Label54.setText(QCoreApplication.translate("Home", u"\u8ba2\u5355\u91d1\u989d", None))
        self.Label8.setText(QCoreApplication.translate("Home", u"\u4e1a\u52a1\u5458", None))
        self.Label_2.setText(QCoreApplication.translate("Home", u"\u4ef7\u7a0e", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Home", u"\u83dc\u5355", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Home", u"\u6211\u7684\u7ecf\u7ba1", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Home", u"\u626b\u7801\u4efb\u52a1", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("Home", u"TextLabel", None))
        self.menu.setTitle(QCoreApplication.translate("Home", u"\u7cfb\u7edf", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Home", u"toolBar", None))
    # retranslateUi

