# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StudyWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StudyWindow(object):
    def setupUi(self, StudyWindow):
        if not StudyWindow.objectName():
            StudyWindow.setObjectName(u"StudyWindow")
        StudyWindow.resize(189, 164)
        self.gridLayout = QGridLayout(StudyWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TimerDisplay = QLCDNumber(StudyWindow)
        self.TimerDisplay.setObjectName(u"TimerDisplay")
        self.TimerDisplay.setDigitCount(8)

        self.gridLayout.addWidget(self.TimerDisplay, 0, 0, 1, 1)

        self.StopButton = QPushButton(StudyWindow)
        self.StopButton.setObjectName(u"StopButton")

        self.gridLayout.addWidget(self.StopButton, 1, 0, 1, 1)


        self.retranslateUi(StudyWindow)

        QMetaObject.connectSlotsByName(StudyWindow)
    # setupUi

    def retranslateUi(self, StudyWindow):
        StudyWindow.setWindowTitle(QCoreApplication.translate("StudyWindow", u"Study", None))
        self.StopButton.setText(QCoreApplication.translate("StudyWindow", u"Stop", None))
    # retranslateUi

