# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'date_range.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_DateRange(object):
    def setupUi(self, DateRange):
        if not DateRange.objectName():
            DateRange.setObjectName(u"DateRange")
        DateRange.resize(429, 179)
        self.horizontalLayout = QHBoxLayout(DateRange)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.begin = QDateEdit(DateRange)
        self.begin.setObjectName(u"begin")
        self.begin.setFocusPolicy(Qt.ClickFocus)
        self.begin.setCurrentSection(QDateTimeEdit.DaySection)
        self.begin.setCalendarPopup(True)
        self.begin.setCurrentSectionIndex(2)

        self.horizontalLayout.addWidget(self.begin)

        self.label = QLabel(DateRange)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(14, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.end = QDateEdit(DateRange)
        self.end.setObjectName(u"end")
        self.end.setFocusPolicy(Qt.ClickFocus)
        self.end.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.end)


        self.retranslateUi(DateRange)
        self.begin.dateChanged.connect(DateRange.beginChanged)
        self.end.dateChanged.connect(DateRange.endChanged)

        QMetaObject.connectSlotsByName(DateRange)
    # setupUi

    def retranslateUi(self, DateRange):
        DateRange.setWindowTitle(QCoreApplication.translate("DateRange", u"Form", None))
        self.begin.setDisplayFormat(QCoreApplication.translate("DateRange", u"yyyy-MM-dd", None))
        self.label.setText(QCoreApplication.translate("DateRange", u"\u81f3", None))
        self.end.setDisplayFormat(QCoreApplication.translate("DateRange", u"yyyy-MM-dd", None))
    # retranslateUi

