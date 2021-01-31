import sys
from PyQt5 import QtGui, QtWidgets

def MyWindow():                                 # a function for the window
    app = QtWidgets.QApplication(sys.argv)      # starting loop
    window = QtWidgets.QWidget()                # window created
    window.setWindowTitle("PyQt5 Gradient")
    window.setGeometry(500,300,250,95)         # (x, y) screen position fixing and window's (breadth, height)
    window.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))

    button = QtWidgets.QPushButton(window)
    button.setText("PyQt5 GUI Programming")
    button.setGeometry(25,15,200,65)
    button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218)); border-radius : 12; border : 2px solid black; color:white; font-size: 14px;")

    window.show()                               # to display
    sys.exit(app.exec())                        # closing the loop

MyWindow()                                      # calling the function block