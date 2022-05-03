from PySide2.QtWidgets import QApplication
from MenuWindowClass import MenuWindow
import sys
import os
import serial

def guiMain(args):
    app = QApplication(args)

    window = MenuWindow()
    window.show()

    return app.exec_()


if __name__ == "__main__":
    com = serial.Serial('COM5', baudrate = 9600)
    com.write(bytes('1', encoding = 'utf-8'))
    guiMain(sys.argv)
