import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QDialog, QGroupBox, QPushButton, QVBoxLayout

class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Gridlayout"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.initWindow()

    def initWindow(self):

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.gridLayoutCreate()
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.groupBox)
        self.setLayout(vboxLayout)

        self.show()

    def gridLayoutCreate(self):
        self.groupBox = QGroupBox("Grid Layout Example")
        gridLayout = QGridLayout()
        gridLayout.addWidget(QPushButton('1'), 0, 0)
        gridLayout.addWidget(QPushButton('2'), 0, 1)
        gridLayout.addWidget(QPushButton('3'), 1, 0)
        gridLayout.addWidget(QPushButton('4'), 1, 1)
        gridLayout.addWidget(QPushButton('5'), 2, 0)
        gridLayout.addWidget(QPushButton('6'), 2, 1)
        self.groupBox.setLayout(gridLayout)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())