# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        if not AddWindow.objectName():
            AddWindow.setObjectName(u"AddWindow")
        AddWindow.resize(222, 152)
        self.gridLayout = QGridLayout(AddWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.newProgram = QTextEdit(AddWindow)
        self.newProgram.setObjectName(u"newProgram")

        self.gridLayout.addWidget(self.newProgram, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AddWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(AddWindow)
        self.buttonBox.accepted.connect(AddWindow.accept)
        self.buttonBox.rejected.connect(AddWindow.reject)

        QMetaObject.connectSlotsByName(AddWindow)
    # setupUi

    def retranslateUi(self, AddWindow):
        AddWindow.setWindowTitle(QCoreApplication.translate("AddWindow", u"Add Program", None))
    # retranslateUi

