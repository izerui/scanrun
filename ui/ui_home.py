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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Home_Form(object):
    def setupUi(self, Home_Form):
        if not Home_Form.objectName():
            Home_Form.setObjectName(u"Home_Form")
        Home_Form.resize(640, 480)
        self.verticalLayoutWidget = QWidget(Home_Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 591, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Home_Form)

        QMetaObject.connectSlotsByName(Home_Form)
    # setupUi

    def retranslateUi(self, Home_Form):
        Home_Form.setWindowTitle(QCoreApplication.translate("Home_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Home_Form", u"\u767b\u5f55\u6210\u529f", None))
    # retranslateUi

