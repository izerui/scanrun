# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import images_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(428, 274)
        icon = QIcon()
        icon.addFile(u":/logo/pic/scanIco.png", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.logo_2 = QLabel(self.widget_2)
        self.logo_2.setObjectName(u"logo_2")

        self.horizontalLayout_2.addWidget(self.logo_2)

        self.title_2 = QLabel(self.widget_2)
        self.title_2.setObjectName(u"title_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.title_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.title_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(125, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.formFrame = QFrame(self.widget)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setFocusPolicy(Qt.StrongFocus)
        self.formFrame.setLayoutDirection(Qt.LeftToRight)
        self.formFrame.setAutoFillBackground(False)
        self.formFrame.setInputMethodHints(Qt.ImhNone)
        self.formFrame.setFrameShadow(QFrame.Plain)
        self.formFrame.setLineWidth(1)
        self.formLayout_3 = QFormLayout(self.formFrame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setHorizontalSpacing(20)
        self.formLayout_3.setVerticalSpacing(20)
        self.formLayout_3.setContentsMargins(12, 12, 12, 12)
        self.Label_3 = QLabel(self.formFrame)
        self.Label_3.setObjectName(u"Label_3")
        font1 = QFont()
        font1.setPointSize(16)
        self.Label_3.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Label_3)

        self.usernameInput = QLineEdit(self.formFrame)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.usernameInput)

        self.Label_4 = QLabel(self.formFrame)
        self.Label_4.setObjectName(u"Label_4")
        self.Label_4.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.Label_4)

        self.passwordInput = QLineEdit(self.formFrame)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setFont(font1)
        self.passwordInput.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.passwordInput)


        self.gridLayout_2.addWidget(self.formFrame, 1, 0, 1, 4)

        self.subButton = QPushButton(self.widget)
        self.subButton.setObjectName(u"subButton")
        self.subButton.setEnabled(False)
        self.subButton.setMinimumSize(QSize(0, 0))
        self.subButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        iconThemeName = u"audio-card"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/logo/pic/login.png", QSize(), QIcon.Normal, QIcon.On)
        
        self.subButton.setIcon(icon1)

        self.gridLayout_2.addWidget(self.subButton, 2, 1, 1, 1)

        self.outButton = QPushButton(self.widget)
        self.outButton.setObjectName(u"outButton")
        self.outButton.setMinimumSize(QSize(0, 0))
        self.outButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/logo/pic/logout.png", QSize(), QIcon.Normal, QIcon.On)
        self.outButton.setIcon(icon2)

        self.gridLayout_2.addWidget(self.outButton, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(126, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.Label_3.setBuddy(self.usernameInput)
        self.Label_4.setBuddy(self.passwordInput)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.usernameInput, self.passwordInput)
        QWidget.setTabOrder(self.passwordInput, self.subButton)
        QWidget.setTabOrder(self.subButton, self.outButton)
        QWidget.setTabOrder(self.outButton, self.formFrame)

        self.retranslateUi(Login)
        self.passwordInput.textChanged.connect(Login.changeButtonState)
        self.subButton.clicked.connect(Login.login)
        self.usernameInput.textChanged.connect(Login.changeButtonState)
        self.outButton.clicked.connect(Login.exist)
        self.passwordInput.returnPressed.connect(Login.login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"\u626b\u7801\u88c5\u7bb1\u7a0b\u5e8f-\u767b\u5f55", None))
        self.logo_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><img width='42' height='42'  src=\":/logo/pic/logo.png\"/></p></body></html>", None))
        self.title_2.setText(QCoreApplication.translate("Login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Academy Engraved LET'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u626b\u7801\u88c5\u7bb1\u7a0b\u5e8f</p></body></html>", None))
        self.Label_3.setText(QCoreApplication.translate("Login", u"\u624b\u673a:", None))
        self.Label_4.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801:", None))
        self.subButton.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.outButton.setText(QCoreApplication.translate("Login", u"\u9000\u51fa", None))
    # retranslateUi

