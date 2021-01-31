import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox

class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layouts"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 600
        self.initWindow()

    def initWindow(self):

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.HorizontalLayout()
        vBox = QVBoxLayout()
        vBox.addWidget(self.groupBox)
        self.setLayout(vBox)

        self.show()

    def HorizontalLayout(self):
        self.groupBox = QGroupBox("What is Sport")
        hBoxLayout = QHBoxLayout()

        button1 = QPushButton("FOOTBALL", self)
        button1.resize(600,50)
        hBoxLayout.addWidget(button1)
        button2 = QPushButton("CRICKET", self)
        hBoxLayout.addWidget(button2)
        button3 = QPushButton("TENNIS", self)
        hBoxLayout.addWidget(button3)

        self.groupBox.setLayout(hBoxLayout)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())