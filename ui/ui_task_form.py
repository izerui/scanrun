# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TaskForm(object):
    def setupUi(self, TaskForm):
        if not TaskForm.objectName():
            TaskForm.setObjectName(u"TaskForm")
        TaskForm.setWindowModality(Qt.NonModal)
        TaskForm.resize(376, 172)
        TaskForm.setModal(True)
        self.gridLayout = QGridLayout(TaskForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(TaskForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1, Qt.AlignBottom)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.banzu = QComboBox(TaskForm)
        self.banzu.setObjectName(u"banzu")

        self.gridLayout_2.addWidget(self.banzu, 1, 1, 1, 1)

        self.chejian = QComboBox(TaskForm)
        self.chejian.setObjectName(u"chejian")

        self.gridLayout_2.addWidget(self.chejian, 0, 1, 1, 1)

        self.Label = QLabel(TaskForm)
        self.Label.setObjectName(u"Label")
        self.Label.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.Label, 0, 0, 1, 1)

        self.Label_3 = QLabel(TaskForm)
        self.Label_3.setObjectName(u"Label_3")
        self.Label_3.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.Label_3, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(TaskForm)
        self.buttonBox.accepted.connect(TaskForm.accept)
        self.buttonBox.rejected.connect(TaskForm.reject)
        self.chejian.currentTextChanged.connect(TaskForm.deptSelected)

        QMetaObject.connectSlotsByName(TaskForm)
    # setupUi

    def retranslateUi(self, TaskForm):
        TaskForm.setWindowTitle(QCoreApplication.translate("TaskForm", u"\u51c6\u5907\u5f00\u59cb\u626b\u7801", None))
        self.Label.setText(QCoreApplication.translate("TaskForm", u"\u8f66  \u95f4:", None))
        self.Label_3.setText(QCoreApplication.translate("TaskForm", u"\u73ed  \u7ec4:", None))
    # retranslateUi

