# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(640, 480)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(120, 100, 421, 251))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.usernameInput = QLineEdit(self.gridLayoutWidget)
        self.usernameInput.setObjectName(u"usernameInput")

        self.gridLayout.addWidget(self.usernameInput, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.passwordInput = QLineEdit(self.gridLayoutWidget)
        self.passwordInput.setObjectName(u"passwordInput")

        self.gridLayout.addWidget(self.passwordInput, 1, 1, 1, 1)

        self.subButton = QPushButton(Form)
        self.subButton.setObjectName(u"subButton")
        self.subButton.setEnabled(False)
        self.subButton.setGeometry(QRect(410, 370, 100, 32))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.usernameInput)
        self.label_2.setBuddy(self.passwordInput)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.usernameInput, self.passwordInput)
        QWidget.setTabOrder(self.passwordInput, self.subButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.subButton.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4", None))
    # retranslateUi

