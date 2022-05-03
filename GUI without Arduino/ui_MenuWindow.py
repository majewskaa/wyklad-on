# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(442, 349)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"Bitstream Vera Sans Mono")
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setLayoutDirection(Qt.LeftToRight)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)

        self.ProgramListTitle = QLabel(self.centralwidget)
        self.ProgramListTitle.setObjectName(u"ProgramListTitle")
        font1 = QFont()
        font1.setFamily(u"Bitstream Vera Sans Mono")
        font1.setPointSize(10)
        self.ProgramListTitle.setFont(font1)

        self.gridLayout.addWidget(self.ProgramListTitle, 1, 0, 1, 1)

        self.ProgramList = QListWidget(self.centralwidget)
        self.ProgramList.setObjectName(u"ProgramList")

        self.gridLayout.addWidget(self.ProgramList, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.AddProgram = QPushButton(self.centralwidget)
        self.AddProgram.setObjectName(u"AddProgram")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddProgram.sizePolicy().hasHeightForWidth())
        self.AddProgram.setSizePolicy(sizePolicy)
        self.AddProgram.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.AddProgram)

        self.DeleteProgram = QPushButton(self.centralwidget)
        self.DeleteProgram.setObjectName(u"DeleteProgram")
        sizePolicy.setHeightForWidth(self.DeleteProgram.sizePolicy().hasHeightForWidth())
        self.DeleteProgram.setSizePolicy(sizePolicy)
        self.DeleteProgram.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.DeleteProgram)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")

        self.horizontalLayout.addWidget(self.StartButton)

        self.HardButton = QPushButton(self.centralwidget)
        self.HardButton.setObjectName(u"HardButton")
        self.HardButton.setAutoFillBackground(False)
        self.HardButton.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.HardButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 442, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Study Buddy", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Study Buddy", None))
        self.ProgramListTitle.setText(QCoreApplication.translate("MainWindow", u"Study-Friendly Programs:", None))
        self.AddProgram.setText(QCoreApplication.translate("MainWindow", u"Add ", None))
        self.DeleteProgram.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.HardButton.setText(QCoreApplication.translate("MainWindow", u"Hard Mode", None))
    # retranslateUi

