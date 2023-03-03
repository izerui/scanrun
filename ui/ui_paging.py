# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paging.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_PagingWidget(object):
    def setupUi(self, PagingWidget):
        if not PagingWidget.objectName():
            PagingWidget.setObjectName(u"PagingWidget")
        PagingWidget.resize(741, 130)
        self.horizontalLayout_2 = QHBoxLayout(PagingWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(PagingWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.line_6 = QFrame(PagingWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_6)

        self.toolButton_7 = QToolButton(PagingWidget)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setMinimumSize(QSize(24, 24))
        self.toolButton_7.setMaximumSize(QSize(24, 24))
        self.toolButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_7.setFocusPolicy(Qt.ClickFocus)
        icon = QIcon()
        icon.addFile(u":/logo/pic/first.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_7.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton_7)

        self.toolButton_8 = QToolButton(PagingWidget)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setMinimumSize(QSize(0, 24))
        self.toolButton_8.setMaximumSize(QSize(24, 24))
        self.toolButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_8.setFocusPolicy(Qt.ClickFocus)
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/pre.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_8.setIcon(icon1)

        self.horizontalLayout.addWidget(self.toolButton_8)

        self.toolButton_9 = QToolButton(PagingWidget)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setMinimumSize(QSize(0, 24))
        self.toolButton_9.setMaximumSize(QSize(24, 24))
        self.toolButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_9.setFocusPolicy(Qt.ClickFocus)
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_9.setIcon(icon2)

        self.horizontalLayout.addWidget(self.toolButton_9)

        self.toolButton_10 = QToolButton(PagingWidget)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setMinimumSize(QSize(0, 24))
        self.toolButton_10.setMaximumSize(QSize(24, 24))
        self.toolButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_10.setFocusPolicy(Qt.ClickFocus)
        icon3 = QIcon()
        icon3.addFile(u":/logo/pic/end.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_10.setIcon(icon3)

        self.horizontalLayout.addWidget(self.toolButton_10)

        self.line_5 = QFrame(PagingWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.toolButton_11 = QToolButton(PagingWidget)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setMinimumSize(QSize(0, 24))
        self.toolButton_11.setMaximumSize(QSize(24, 24))
        self.toolButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_11.setFocusPolicy(Qt.ClickFocus)
        icon4 = QIcon()
        icon4.addFile(u":/logo/pic/jump.png", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton_11.setIcon(icon4)

        self.horizontalLayout.addWidget(self.toolButton_11)

        self.pageEdit = QSpinBox(PagingWidget)
        self.pageEdit.setObjectName(u"pageEdit")
        self.pageEdit.setMinimumSize(QSize(0, 24))
        self.pageEdit.setMaximumSize(QSize(16777215, 24))
        self.pageEdit.setFocusPolicy(Qt.ClickFocus)
        self.pageEdit.setMaximum(9999)
        self.pageEdit.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.pageEdit.setDisplayIntegerBase(10)

        self.horizontalLayout.addWidget(self.pageEdit)

        self.label = QLabel(PagingWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line_7 = QFrame(PagingWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_7)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(PagingWidget)
        self.toolButton_7.clicked.connect(PagingWidget.firstPage)
        self.toolButton_8.clicked.connect(PagingWidget.prePage)
        self.toolButton_9.clicked.connect(PagingWidget.nextPage)
        self.toolButton_10.clicked.connect(PagingWidget.endPage)
        self.toolButton_11.clicked.connect(PagingWidget.jumpPage)

        QMetaObject.connectSlotsByName(PagingWidget)
    # setupUi

    def retranslateUi(self, PagingWidget):
        PagingWidget.setWindowTitle(QCoreApplication.translate("PagingWidget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("PagingWidget", u"--", None))
#if QT_CONFIG(tooltip)
        self.toolButton_7.setToolTip(QCoreApplication.translate("PagingWidget", u"\u9996\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_7.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_8.setToolTip(QCoreApplication.translate("PagingWidget", u"\u4e0a\u4e00\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_8.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_9.setToolTip(QCoreApplication.translate("PagingWidget", u"\u4e0b\u4e00\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_9.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_10.setToolTip(QCoreApplication.translate("PagingWidget", u"\u672b\u9875", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_10.setText("")
#if QT_CONFIG(tooltip)
        self.toolButton_11.setToolTip(QCoreApplication.translate("PagingWidget", u"\u8df3\u8f6c\u5230", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_11.setText("")
        self.label.setText(QCoreApplication.translate("PagingWidget", u"\u9875", None))
    # retranslateUi

