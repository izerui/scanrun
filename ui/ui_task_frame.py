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
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
import images_rc

class Ui_TaskFrame(object):
    def setupUi(self, TaskFrame):
        if not TaskFrame.objectName():
            TaskFrame.setObjectName(u"TaskFrame")
        TaskFrame.resize(860, 682)
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
        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        if (self.tableWidget.columnCount() < 21):
            self.tableWidget.setColumnCount(21)
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
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableWidget)

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
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 819, 667))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_3.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_3.setHorizontalSpacing(3)
        self.formLayout_3.setVerticalSpacing(-1)
        self.Label_3 = QLabel(self.scrollAreaWidgetContents)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Label_3)

        self.saleOrderDocNo = QLineEdit(self.scrollAreaWidgetContents)
        self.saleOrderDocNo.setObjectName(u"saleOrderDocNo")
        self.saleOrderDocNo.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.saleOrderDocNo)

        self.Label2_2 = QLabel(self.scrollAreaWidgetContents)
        self.Label2_2.setObjectName(u"Label2_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.Label2_2)

        self.customerSerial = QLineEdit(self.scrollAreaWidgetContents)
        self.customerSerial.setObjectName(u"customerSerial")
        self.customerSerial.setEnabled(True)
        self.customerSerial.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.customerSerial)

        self.Label3_2 = QLabel(self.scrollAreaWidgetContents)
        self.Label3_2.setObjectName(u"Label3_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.Label3_2)

        self.customerName = QLineEdit(self.scrollAreaWidgetContents)
        self.customerName.setObjectName(u"customerName")
        self.customerName.setEnabled(True)
        self.customerName.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.customerName)

        self.Label54_2 = QLabel(self.scrollAreaWidgetContents)
        self.Label54_2.setObjectName(u"Label54_2")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.Label54_2)

        self.customerOrderDocNo = QLineEdit(self.scrollAreaWidgetContents)
        self.customerOrderDocNo.setObjectName(u"customerOrderDocNo")
        self.customerOrderDocNo.setEnabled(True)
        self.customerOrderDocNo.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.customerOrderDocNo)

        self.Label8_2 = QLabel(self.scrollAreaWidgetContents)
        self.Label8_2.setObjectName(u"Label8_2")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.Label8_2)

        self.inventoryCode = QLineEdit(self.scrollAreaWidgetContents)
        self.inventoryCode.setObjectName(u"inventoryCode")
        self.inventoryCode.setEnabled(True)
        self.inventoryCode.setReadOnly(True)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.inventoryCode)

        self.Label_4 = QLabel(self.scrollAreaWidgetContents)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.Label_4)

        self.inventoryName = QLineEdit(self.scrollAreaWidgetContents)
        self.inventoryName.setObjectName(u"inventoryName")
        self.inventoryName.setEnabled(True)
        self.inventoryName.setReadOnly(True)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.inventoryName)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label)

        self.inventorySpec = QLineEdit(self.scrollAreaWidgetContents)
        self.inventorySpec.setObjectName(u"inventorySpec")
        self.inventorySpec.setEnabled(True)
        self.inventorySpec.setReadOnly(True)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.inventorySpec)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_3)

        self.unitName = QLineEdit(self.scrollAreaWidgetContents)
        self.unitName.setObjectName(u"unitName")
        self.unitName.setEnabled(True)
        self.unitName.setReadOnly(True)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.unitName)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_4)

        self.customerMaterialCode = QLineEdit(self.scrollAreaWidgetContents)
        self.customerMaterialCode.setObjectName(u"customerMaterialCode")
        self.customerMaterialCode.setEnabled(True)
        self.customerMaterialCode.setReadOnly(True)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.customerMaterialCode)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.label_5)

        self.customerInventoryName = QLineEdit(self.scrollAreaWidgetContents)
        self.customerInventoryName.setObjectName(u"customerInventoryName")
        self.customerInventoryName.setEnabled(True)
        self.customerInventoryName.setReadOnly(True)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.customerInventoryName)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.label_6)

        self.customerInventorySpec = QLineEdit(self.scrollAreaWidgetContents)
        self.customerInventorySpec.setObjectName(u"customerInventorySpec")
        self.customerInventorySpec.setEnabled(True)
        self.customerInventorySpec.setReadOnly(True)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.customerInventorySpec)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.label_7)

        self.employeeName = QLineEdit(self.scrollAreaWidgetContents)
        self.employeeName.setObjectName(u"employeeName")
        self.employeeName.setEnabled(True)
        self.employeeName.setReadOnly(True)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.employeeName)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.label_8)

        self.creatorName = QLineEdit(self.scrollAreaWidgetContents)
        self.creatorName.setObjectName(u"creatorName")
        self.creatorName.setEnabled(True)
        self.creatorName.setReadOnly(True)

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.creatorName)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.label_10)

        self.createTime = QLineEdit(self.scrollAreaWidgetContents)
        self.createTime.setObjectName(u"createTime")
        self.createTime.setEnabled(True)
        self.createTime.setReadOnly(True)

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.createTime)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(14, QFormLayout.LabelRole, self.label_11)

        self.deliveryDate = QLineEdit(self.scrollAreaWidgetContents)
        self.deliveryDate.setObjectName(u"deliveryDate")
        self.deliveryDate.setEnabled(True)
        self.deliveryDate.setReadOnly(True)

        self.formLayout_3.setWidget(14, QFormLayout.FieldRole, self.deliveryDate)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(15, QFormLayout.LabelRole, self.label_12)

        self.quantity = QLineEdit(self.scrollAreaWidgetContents)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setEnabled(True)
        self.quantity.setReadOnly(True)

        self.formLayout_3.setWidget(15, QFormLayout.FieldRole, self.quantity)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(16, QFormLayout.LabelRole, self.label_9)

        self.taskQuantity = QLineEdit(self.scrollAreaWidgetContents)
        self.taskQuantity.setObjectName(u"taskQuantity")
        self.taskQuantity.setReadOnly(True)

        self.formLayout_3.setWidget(16, QFormLayout.FieldRole, self.taskQuantity)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(17, QFormLayout.LabelRole, self.label_13)

        self.scanCodeQuantity = QLineEdit(self.scrollAreaWidgetContents)
        self.scanCodeQuantity.setObjectName(u"scanCodeQuantity")
        self.scanCodeQuantity.setReadOnly(True)

        self.formLayout_3.setWidget(17, QFormLayout.FieldRole, self.scanCodeQuantity)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(18, QFormLayout.LabelRole, self.label_14)

        self.waitScanCodeQuantity = QLineEdit(self.scrollAreaWidgetContents)
        self.waitScanCodeQuantity.setObjectName(u"waitScanCodeQuantity")
        self.waitScanCodeQuantity.setReadOnly(True)

        self.formLayout_3.setWidget(18, QFormLayout.FieldRole, self.waitScanCodeQuantity)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(19, QFormLayout.LabelRole, self.label_15)

        self.boxQuantity = QLineEdit(self.scrollAreaWidgetContents)
        self.boxQuantity.setObjectName(u"boxQuantity")
        self.boxQuantity.setReadOnly(True)

        self.formLayout_3.setWidget(19, QFormLayout.FieldRole, self.boxQuantity)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(20, QFormLayout.LabelRole, self.label_16)

        self.palletQuantity = QLineEdit(self.scrollAreaWidgetContents)
        self.palletQuantity.setObjectName(u"palletQuantity")
        self.palletQuantity.setReadOnly(True)

        self.formLayout_3.setWidget(20, QFormLayout.FieldRole, self.palletQuantity)


        self.verticalLayout_2.addLayout(self.formLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(TaskFrame)
        self.toolButton_8.clicked.connect(TaskFrame.prePage)
        self.tableWidget.itemDoubleClicked.connect(TaskFrame.openTaskForm)
        self.toolButton_10.clicked.connect(TaskFrame.endPage)
        self.toolButton_9.clicked.connect(TaskFrame.nextPage)
        self.toolButton_11.clicked.connect(TaskFrame.jumpPage)
        self.toolButton_7.clicked.connect(TaskFrame.firstPage)
        self.tableWidget.itemSelectionChanged.connect(TaskFrame.dataRowSelected)
        self.pushButton_12.clicked.connect(TaskFrame.openTaskForm)

        QMetaObject.connectSlotsByName(TaskFrame)
    # setupUi

    def retranslateUi(self, TaskFrame):
        TaskFrame.setWindowTitle(QCoreApplication.translate("TaskFrame", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TaskFrame", u"\u9500\u552e\u5355\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u7f16\u7801", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u8ba2\u5355\u53f7", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TaskFrame", u"\u8d27\u54c1\u7f16\u7801", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TaskFrame", u"\u8d27\u54c1\u540d\u79f0", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TaskFrame", u"\u89c4\u683c\u578b\u53f7", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TaskFrame", u"\u5355\u4f4d", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u6599\u53f7", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u54c1\u540d", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u578b\u53f7", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TaskFrame", u"\u4e1a\u52a1\u5458", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("TaskFrame", u"\u4efb\u52a1\u521b\u5efa\u4eba", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("TaskFrame", u"\u4efb\u52a1\u521b\u5efa\u65e5\u671f", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("TaskFrame", u"\u8ba2\u5355\u4ea4\u671f", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("TaskFrame", u"\u9500\u552e\u8ba2\u5355\u6570\u91cf", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("TaskFrame", u"\u4efb\u52a1\u6570\u91cf", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("TaskFrame", u"\u5df2\u626b\u7801\u6570\u91cf", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("TaskFrame", u"\u672a\u626b\u7801\u6570\u91cf", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("TaskFrame", u"\u88c5\u7bb1\u6570\u91cf", None));
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("TaskFrame", u"\u5361\u677f\u6570\u91cf", None));
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
        self.saleOrderDocNo.setText("")
        self.Label2_2.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u7f16\u7801", None))
        self.Label3_2.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u540d\u79f0", None))
        self.Label54_2.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u8ba2\u5355\u53f7", None))
        self.Label8_2.setText(QCoreApplication.translate("TaskFrame", u"\u8d27\u54c1\u7f16\u7801", None))
        self.Label_4.setText(QCoreApplication.translate("TaskFrame", u"\u8d27\u54c1\u540d\u79f0", None))
        self.label.setText(QCoreApplication.translate("TaskFrame", u"\u89c4\u683c\u578b\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("TaskFrame", u"\u5355\u4f4d", None))
        self.label_4.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u6599\u53f7", None))
        self.label_5.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u54c1\u540d", None))
        self.label_6.setText(QCoreApplication.translate("TaskFrame", u"\u5ba2\u6237\u578b\u53f7", None))
        self.label_7.setText(QCoreApplication.translate("TaskFrame", u"\u4e1a\u52a1\u5458", None))
        self.label_8.setText(QCoreApplication.translate("TaskFrame", u"\u4efb\u52a1\u521b\u5efa\u4eba", None))
        self.label_10.setText(QCoreApplication.translate("TaskFrame", u"\u4efb\u52a1\u521b\u5efa\u65e5\u671f", None))
        self.label_11.setText(QCoreApplication.translate("TaskFrame", u"\u8ba2\u5355\u4ea4\u671f", None))
        self.label_12.setText(QCoreApplication.translate("TaskFrame", u"\u9500\u552e\u8ba2\u5355\u6570\u91cf", None))
        self.label_9.setText(QCoreApplication.translate("TaskFrame", u"\u4efb\u52a1\u6570\u91cf", None))
        self.label_13.setText(QCoreApplication.translate("TaskFrame", u"\u5df2\u626b\u7801\u6570\u91cf", None))
        self.label_14.setText(QCoreApplication.translate("TaskFrame", u"\u672a\u626b\u7801\u6570\u91cf", None))
        self.label_15.setText(QCoreApplication.translate("TaskFrame", u"\u88c5\u7bb1\u6570\u91cf", None))
        self.label_16.setText(QCoreApplication.translate("TaskFrame", u"\u5361\u677f\u6570\u91cf", None))
    # retranslateUi

