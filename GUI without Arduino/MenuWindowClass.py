from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtCore import QTimer
from ui_MenuWindow import Ui_MainWindow
from StudyWindowClass import StudyWindow
from AddWindowClass import AddWindow
from PySide2.QtCore import Qt
import win32gui
import os


class MenuWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupMenu()

    def setupMenu(self):
        self.ui.ProgramList.addItem('Microsoft Teams')

        self.ui.StartButton.clicked.connect(self.study)
        self.ui.HardButton.clicked.connect(self.hardStudy)
        self.ui.AddProgram.clicked.connect(self.addingProgram)
        self.ui.DeleteProgram.clicked.connect(self.deleteProgram)

    def study(self):
        self.hide()

        studyWindow = StudyWindow()

        self.box = QMessageBox()
        self.box.setText('Get back to study!')
        self.box.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.timer = QTimer()
        self.startTimer()
        self.timer.timeout.connect(self.controlStudy)

        studyWindow.finished.connect(self.endStudy)
        studyWindow.exec()

    def controlStudy(self):
        w = win32gui
        window_name = w.GetWindowText(w.GetForegroundWindow())

        apps = self.getAllowedApps()
        if not any(app in window_name for app in apps):

            self.box.exec()

    def startTimer(self):
        self.time = 0
        self.timer.start(1000)

    def endStudy(self):
        self.timer.stop()
        self.show()

    def getAllowedApps(self):
        ProgramList = self.ui.ProgramList
        items = []
        for x in range(ProgramList.count()):
            items.append(ProgramList.item(x).text())
        items.append('Study')
        return items

    def hardStudy(self):
        self.hide()
        os.system("AutoHotkey.exe anti-distractorv3.ahk")

    def addingProgram(self):
        self.addWindow = AddWindow()
        self.addWindow.window.buttonBox.accepted.connect(self.addProgram)
        self.addWindow.exec()

    def addProgram(self):
        programName = self.addWindow.getText()
        if programName:
            self.ui.ProgramList.addItem(programName)

    def deleteProgram(self):
        items = self.ui.ProgramList.selectedItems()
        for item in items:
            self.ui.ProgramList.takeItem(self.ui.ProgramList.row(item))
