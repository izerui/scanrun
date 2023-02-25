# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import images_rc

class Ui_Login_Form(object):
    def setupUi(self, Login_Form):
        if not Login_Form.objectName():
            Login_Form.setObjectName(u"Login_Form")
        Login_Form.setEnabled(True)
        Login_Form.resize(509, 342)
        Login_Form.setMinimumSize(QSize(509, 342))
        Login_Form.setMaximumSize(QSize(509, 342))
        self.gridLayout_2 = QGridLayout(Login_Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Login_Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.usernameInput = QLineEdit(self.frame)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setGeometry(QRect(200, 102, 150, 21))
        self.usernameInput.setMaxLength(24)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 100, 71, 21))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.subButton = QPushButton(self.frame)
        self.subButton.setObjectName(u"subButton")
        self.subButton.setEnabled(False)
        self.subButton.setGeometry(QRect(130, 210, 100, 42))
        self.subButton.setMinimumSize(QSize(0, 42))
        self.subButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        iconThemeName = u"audio-card"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/logo/pic/login.png", QSize(), QIcon.Normal, QIcon.On)

        self.subButton.setIcon(icon)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 160, 71, 21))
        self.label_2.setFont(font)
        self.passwordInput = QLineEdit(self.frame)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(200, 160, 150, 21))
        self.passwordInput.setMaxLength(24)
        self.passwordInput.setFrame(True)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.outButton = QPushButton(self.frame)
        self.outButton.setObjectName(u"outButton")
        self.outButton.setGeometry(QRect(250, 210, 100, 42))
        self.outButton.setMinimumSize(QSize(0, 42))
        self.outButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/logo/pic/logout.png", QSize(), QIcon.Normal, QIcon.On)
        self.outButton.setIcon(icon1)
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(180, 40, 161, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Academy Engraved LET"])
        font1.setPointSize(24)
        font1.setBold(False)
        self.title.setFont(font1)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(121, 40, 41, 41))
        self.process_label = QLabel(self.frame)
        self.process_label.setObjectName(u"process_label")
        self.process_label.setGeometry(QRect(190, 250, 90, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.process_label.setFont(font2)
        self.process_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.usernameInput)
        self.label_2.setBuddy(self.passwordInput)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Login_Form)
        self.usernameInput.textEdited.connect(Login_Form.changeButtonState)
        self.passwordInput.textEdited.connect(Login_Form.changeButtonState)
        self.subButton.clicked.connect(Login_Form.loginForm)
        self.outButton.clicked.connect(Login_Form.existForm)

        QMetaObject.connectSlotsByName(Login_Form)
    # setupUi

    def retranslateUi(self, Login_Form):
        Login_Form.setWindowTitle(QCoreApplication.translate("Login_Form", u"SN\u5e8f\u5217\u53f7\u626b\u7801\u88c5\u7bb1\u7cfb\u7edf-\u767b\u5f55\u9875\u9762", None))
        self.usernameInput.setText(QCoreApplication.translate("Login_Form", u"18814128446", None))
        self.label.setText(QCoreApplication.translate("Login_Form", u"\u7528\u6237\u540d\uff1a", None))
        self.subButton.setText(QCoreApplication.translate("Login_Form", u"\u767b\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("Login_Form", u"\u5bc6    \u7801\uff1a", None))
        self.passwordInput.setText(QCoreApplication.translate("Login_Form", u"woshichaojimima001", None))
        self.passwordInput.setPlaceholderText("")
        self.outButton.setText(QCoreApplication.translate("Login_Form", u"\u9000\u51fa", None))
        self.title.setText(QCoreApplication.translate("Login_Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Academy Engraved LET'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u626b\u7801\u88c5\u7bb1\u7a0b\u5e8f</p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("Login_Form", u"<html><head/><body><p><img width='42' height='42'  src=\":/logo/pic/logo.png\"/></p></body></html>", None))
        self.process_label.setText(QCoreApplication.translate("Login_Form", u"\u6b63\u5728\u767b\u9646...", None))
    # retranslateUi

