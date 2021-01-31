import sys
import time
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):                                 # Constructor
        super(Window,self).__init__()

        self.initWindow()                               # Calling the function written

    def initWindow(self):

        self.lineEdit = QtWidgets.QLineEdit();          # To enter any text
        self.button1 = QtWidgets.QPushButton("Print");
        self.button2 = QtWidgets.QPushButton("Clear");
        self.button1.setStyleSheet("QPushButton::pressed{color:white; font-size: 20px; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0CBA1E, stop:1 #02A812);border-radius : 3 }")

        vBox = QtWidgets.QVBoxLayout()                  # Using vertical layout
        vBox.addWidget(self.lineEdit)                   # Adding items
        vBox.addWidget(self.button1)
        vBox.addWidget(self.button2)

        self.setLayout(vBox)
        self.setWindowTitle("PyQt5")
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))

        self.button1.clicked.connect(self.btnClicked)   # case 1
        self.button2.clicked.connect(self.btnClicked)   # case 2

        self.show()

    def btnClicked(self):
        sender = self.sender()
        if sender.text() == "Print":        # case 1
            print(self.lineEdit.text())     # Displays entered text in output window if 'Print' button is clicked
            self.close()
        else:                               # case 2
            self.lineEdit.clear()           # Clears otherwise

app = QtWidgets.QApplication(sys.argv)
ourWindow = Window()
sys.exit(app.exec())