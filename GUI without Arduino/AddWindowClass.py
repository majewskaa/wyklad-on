from PySide2.QtWidgets import QDialog
from ui_AddWindow import Ui_AddWindow


class AddWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = Ui_AddWindow()
        self.window.setupUi(self)

    def getText(self):
        return self.window.newProgram.toPlainText()
