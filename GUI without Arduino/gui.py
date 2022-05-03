from PySide2.QtWidgets import QApplication
from MenuWindowClass import MenuWindow
import sys

def guiMain(args):
    app = QApplication(args)

    window = MenuWindow()
    window.show()

    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
