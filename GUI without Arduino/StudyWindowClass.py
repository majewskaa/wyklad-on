from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QTimer
from ui_StudyWindow import Ui_StudyWindow


class StudyWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = Ui_StudyWindow()
        self.window.setupUi(self)
        self.setupStudy()

    def setupStudy(self):
        self.window.StopButton.clicked.connect(self.stopStudy)

        self.timer = QTimer()
        self.startTimer()
        self.timer.timeout.connect(self.clock)

    def showTime(self):
        seconds = self.time % 60
        minutes = ((self.time - seconds) % 3600) / 60
        hours = (self.time - seconds) / 3600

        timeText = "%02d:%02d:%02d" % (hours, minutes, seconds)
        self.window.TimerDisplay.display(timeText)

    def startTimer(self):
        self.time = 0
        self.timer.start(1000)

    def clock(self):
        self.time += 1
        self.showTime()

    def endTimer(self):
        self.timer.stop()

    def stopStudy(self):
        self.endTimer()
        self.done(1)
