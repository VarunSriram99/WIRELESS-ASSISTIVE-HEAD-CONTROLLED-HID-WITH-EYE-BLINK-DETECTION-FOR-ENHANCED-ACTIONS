import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):

    def __init__(self):                             # Constructor
        super().__init__()

        self.initWindow()                           # Calling the function written

    def initWindow(self):

        self.label = QtWidgets.QLabel("Let us change the text here!")
        self.button1 = QtWidgets.QPushButton("Click Me")
        vBox = QtWidgets.QVBoxLayout()

        vBox.addWidget(self.label)
        vBox.addWidget(self.button1)

        self.setLayout(vBox)

        self.setWindowTitle("PyQt App")
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))

        self.button1.clicked.connect(self.btnClicked)

        self.show()

    def btnClicked(self):                            # When a button click happens,
        self.label.setText("THE TEXT HAS BEEN CHANGED!")       # Update the label text
        self.label.setFont(QtGui.QFont('Arial', 25))

app = QtWidgets.QApplication(sys.argv)
ourWindow = Window()
sys.exit(app.exec())