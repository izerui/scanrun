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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QTableView, QToolButton,
    QVBoxLayout, QWidget)
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
        self.gridLayout_2 = QGridLayout(TaskFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(TaskFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.widget_2 = QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.toolButton_7 = QToolButton(self.widget_2)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setMinimumSize(QSize(24, 24))
        self.toolButton_7.setMaximumSize(QSize(24, 24))
        self.toolButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/logo/pic/first.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_7.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.toolButton_7)

        self.toolButton_8 = QToolButton(self.widget_2)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setMinimumSize(QSize(0, 24))
        self.toolButton_8.setMaximumSize(QSize(24, 24))
        self.toolButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/pre.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_8.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.toolButton_8)

        self.toolButton_9 = QToolButton(self.widget_2)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setMinimumSize(QSize(0, 24))
        self.toolButton_9.setMaximumSize(QSize(24, 24))
        self.toolButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_9.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.toolButton_9)

        self.toolButton_10 = QToolButton(self.widget_2)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setMinimumSize(QSize(0, 24))
        self.toolButton_10.setMaximumSize(QSize(24, 24))
        self.toolButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/logo/pic/end.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_10.setIcon(icon3)

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
        icon4 = QIcon()
        icon4.addFile(u":/logo/pic/jump.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_11.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.toolButton_11)

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

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_3.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_3.setHorizontalSpacing(3)
        self.Label_3 = QLabel(self.frame)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Label_3)

        self.LineEdit_7 = QLineEdit(self.frame)
        self.LineEdit_7.setObjectName(u"LineEdit_7")
        self.LineEdit_7.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.LineEdit_7)

        self.Label2_2 = QLabel(self.frame)
        self.Label2_2.setObjectName(u"Label2_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.Label2_2)

        self.LineEdit_11 = QLineEdit(self.frame)
        self.LineEdit_11.setObjectName(u"LineEdit_11")
        self.LineEdit_11.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.LineEdit_11)

        self.Label3_2 = QLabel(self.frame)
        self.Label3_2.setObjectName(u"Label3_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.Label3_2)

        self.LineEdit_8 = QLineEdit(self.frame)
        self.LineEdit_8.setObjectName(u"LineEdit_8")
        self.LineEdit_8.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.LineEdit_8)

        self.Label54_2 = QLabel(self.frame)
        self.Label54_2.setObjectName(u"Label54_2")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.Label54_2)

        self.LineEdit_9 = QLineEdit(self.frame)
        self.LineEdit_9.setObjectName(u"LineEdit_9")
        self.LineEdit_9.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.LineEdit_9)

        self.Label8_2 = QLabel(self.frame)
        self.Label8_2.setObjectName(u"Label8_2")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.Label8_2)

        self.LineEdit_10 = QLineEdit(self.frame)
        self.LineEdit_10.setObjectName(u"LineEdit_10")
        self.LineEdit_10.setReadOnly(True)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.LineEdit_10)

        self.Label_4 = QLabel(self.frame)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.Label_4)

        self.LineEdit_12 = QLineEdit(self.frame)
        self.LineEdit_12.setObjectName(u"LineEdit_12")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.LineEdit_12)


        self.gridLayout.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(TaskFrame)
        self.toolButton_8.clicked.connect(TaskFrame.prePage)
        self.toolButton_10.clicked.connect(TaskFrame.endPage)
        self.toolButton_9.clicked.connect(TaskFrame.nextPage)
        self.toolButton_11.clicked.connect(TaskFrame.jumpPage)
        self.toolButton_7.clicked.connect(TaskFrame.firstPage)
        self.pushButton_12.clicked.connect(TaskFrame.openTaskForm)
        self.tableView.doubleClicked.connect(TaskFrame.openTaskForm)

        QMetaObject.connectSlotsByName(TaskFrame)
    # setupUi

    def retranslateUi(self, TaskFrame):
        TaskFrame.setWindowTitle(QCoreApplication.translate("TaskFrame", u"Form", None))
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

