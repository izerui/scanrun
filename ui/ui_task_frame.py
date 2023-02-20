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
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import images_rc

class Ui_TaskFrame(object):
    def setupUi(self, TaskFrame):
        if not TaskFrame.objectName():
            TaskFrame.setObjectName(u"TaskFrame")
        TaskFrame.resize(823, 574)
        TaskFrame.setStyleSheet(u"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #dcdfe6;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ecf5ff;\n"
"    color: #409eff;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #3a8ee6;\n"
"    color: #409eff;\n"
"}")
        self.verticalLayout = QVBoxLayout(TaskFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(TaskFrame)
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

        self.verticalLayout.addWidget(self.tableWidget)

        self.widget_2 = QWidget(TaskFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(24, 24))
        self.pushButton_7.setMaximumSize(QSize(24, 24))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/logo/pic/first.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_7.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 24))
        self.pushButton_8.setMaximumSize(QSize(24, 24))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/pre.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_8.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 24))
        self.pushButton_9.setMaximumSize(QSize(24, 24))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_9.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 24))
        self.pushButton_10.setMaximumSize(QSize(24, 24))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/logo/pic/end.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_10.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.pushButton_10)

        self.line_5 = QFrame(self.widget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_5)

        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 24))
        self.pushButton_11.setMaximumSize(QSize(24, 24))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/logo/pic/jump.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_11.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.pushButton_11)

        self.pageEdit = QSpinBox(self.widget_2)
        self.pageEdit.setObjectName(u"pageEdit")
        self.pageEdit.setMinimumSize(QSize(0, 24))
        self.pageEdit.setMaximumSize(QSize(16777215, 24))
        self.pageEdit.setMaximum(9999)
        self.pageEdit.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.pageEdit.setDisplayIntegerBase(10)

        self.horizontalLayout_2.addWidget(self.pageEdit)

        self.line_6 = QFrame(self.widget_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_6)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

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
        icon5 = QIcon()
        icon5.addFile(u":/logo/pic/scanIco.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_12)

        self.line_8 = QFrame(self.widget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_8)


        self.verticalLayout.addWidget(self.widget_2)

        self.scrollArea_2 = QScrollArea(TaskFrame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 200))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 782, 202))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_3.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_3.setHorizontalSpacing(3)
        self.Label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Label_3)

        self.LineEdit_7 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_7.setObjectName(u"LineEdit_7")
        self.LineEdit_7.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.LineEdit_7)

        self.Label2_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.Label2_2.setObjectName(u"Label2_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.Label2_2)

        self.Label3_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.Label3_2.setObjectName(u"Label3_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.Label3_2)

        self.LineEdit_8 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_8.setObjectName(u"LineEdit_8")
        self.LineEdit_8.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.LineEdit_8)

        self.Label54_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.Label54_2.setObjectName(u"Label54_2")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.Label54_2)

        self.LineEdit_9 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_9.setObjectName(u"LineEdit_9")
        self.LineEdit_9.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.LineEdit_9)

        self.Label8_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.Label8_2.setObjectName(u"Label8_2")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.Label8_2)

        self.LineEdit_10 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_10.setObjectName(u"LineEdit_10")
        self.LineEdit_10.setReadOnly(True)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.LineEdit_10)

        self.LineEdit_11 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_11.setObjectName(u"LineEdit_11")
        self.LineEdit_11.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.LineEdit_11)

        self.Label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.Label_4)

        self.LineEdit_12 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_12.setObjectName(u"LineEdit_12")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.LineEdit_12)


        self.gridLayout_3.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)


        self.retranslateUi(TaskFrame)
        self.pushButton_7.clicked.connect(TaskFrame.firstPage)
        self.pushButton_8.clicked.connect(TaskFrame.prePage)
        self.pushButton_9.clicked.connect(TaskFrame.nextPage)
        self.pushButton_10.clicked.connect(TaskFrame.endPage)
        self.pushButton_11.clicked.connect(TaskFrame.jumpPage)
        self.pushButton_12.clicked.connect(TaskFrame.openTaskForm)
        self.tableWidget.itemSelectionChanged.connect(TaskFrame.dataRowSelected)

        QMetaObject.connectSlotsByName(TaskFrame)
    # setupUi

    def retranslateUi(self, TaskFrame):
        TaskFrame.setWindowTitle(QCoreApplication.translate("TaskFrame", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TaskFrame", u"\u9500\u552e\u5355\u53f7", u"\u65b9\u6cd5"));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u8ba2\u5355\u53f7", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TaskFrame", u"\u8ba2\u5355\u91d1\u989d", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TaskFrame", u"\u4e1a\u52a1\u5458", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TaskFrame", u"\u521b\u5efa\u65f6\u95f4", None));
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("TaskFrame", u"\u9996\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("TaskFrame", u"\u4e0a\u4e00\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_9.setToolTip(QCoreApplication.translate("TaskFrame", u"\u4e0b\u4e00\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_9.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_10.setToolTip(QCoreApplication.translate("TaskFrame", u"\u672b\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_10.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_11.setToolTip(QCoreApplication.translate("TaskFrame", u"\u8df3\u8f6c\u5230", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_11.setText("")
        self.label_2.setText(QCoreApplication.translate("TaskFrame", u"--", None))
#if QT_CONFIG(tooltip)
        self.pushButton_12.setToolTip(QCoreApplication.translate("TaskFrame", u"\u8bf7\u9009\u62e9\u4e00\u6761\u8bb0\u5f55\u5e76\u5f00\u59cb\u626b\u63cf", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_12.setText(QCoreApplication.translate("TaskFrame", u"\u5f00\u59cb\u626b\u63cf", None))
        self.Label_3.setText(QCoreApplication.translate("TaskFrame", u"\u9500\u552e\u5355\u53f7", None))
        self.LineEdit_7.setText("")
        self.Label2_2.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u540d\u79f0", None))
        self.Label3_2.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u8ba2\u5355\u53f7", None))
        self.Label54_2.setText(QCoreApplication.translate("TaskFrame", u"\u8ba2\u5355\u91d1\u989d", None))
        self.Label8_2.setText(QCoreApplication.translate("TaskFrame", u"\u4e1a\u52a1\u5458", None))
        self.Label_4.setText(QCoreApplication.translate("TaskFrame", u"\u4ef7\u7a0e", None))
    # retranslateUi

