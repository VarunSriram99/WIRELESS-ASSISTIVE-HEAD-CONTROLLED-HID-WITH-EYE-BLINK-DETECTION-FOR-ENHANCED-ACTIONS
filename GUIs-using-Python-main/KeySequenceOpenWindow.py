import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QDesktopWidget, QShortcut

class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.shortcut_open = QShortcut(QKeySequence('Ctrl+T'), self)
        self.shortcut_open.activated.connect(self.on_open)

    def on_open(self):
        self.show()
        #self.setGeometry(300,200,500,400)
        #self.setWindowOpacity(0.85)
        #self.resize(400,400)
        #self.showFullScreen()
        #QWidget.showMaximized(self)
        ##  Here insert code for Directly shifting to Left-Click Mode now (i.e, on opening this window, auto-shift of mode)
        self.center()
        self.setWindowTitle("PyQt5 AT GUI")
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        self.setStyleSheet("background-color: black")
        values = ['Left-Click', '', 'Hover', 'Middle-Click', '', 'Right-Click', 'Scroll', '', 'Drag']
        positions = [(r, c) for r in range(4) for c in range(3)]
        layout = QGridLayout()
        self.setLayout(layout)

        for positions, value in zip(positions, values):
            self.button = QPushButton(value)
            self.button.setStyleSheet("QPushButton{color:black; background-color : white; font-size: 17px; }QPushButton::pressed{background-color : #C0C0C0;}")
            # self.button.setStyleSheet("QPushButton{color:black; background-color : white; font-size: 17px; border: 2px solid blue; border-radius: 10px; }QPushButton::pressed{color:white; background-color : blue;}")
            # self.button.setStyleSheet("color:white; font-size: 17px; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1D1D89, stop:1 #191950); border-radius : 10 ")
            # self.button.setStyleSheet("color:white; font-size: 17px; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #02A812, stop:1 #0C7604); border-radius : 5 ")
            self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout.addWidget(self.button, *positions)
            self.button.clicked.connect(self.btnClicked)
            self.show()

    def btnClicked(self):
        sender = self.sender()
        if sender.text() == "Left-Click":
            #pass
            self.close()
        elif sender.text() == "Hover":
            #pass
            self.close()
        elif sender.text() == "Middle-Click":
            pass
            self.close()
        elif sender.text() == "Right-Click":
            pass
            self.close()
        elif sender.text() == "Scroll":
            pass
            self.close()
        elif sender.text() == "Drag":
            pass
            self.close()

    def center(self):
        ab = QDesktopWidget().screenGeometry()
        w = ab.width()*0.3
        h = ab.height()*0.3
        self.resize(w,h)
        x = 0.5*w
        y = 0.5*h
        self.move((ab.width()/2)-x,(ab.height()/2)-y)

def main():
    app = QApplication(sys.argv)
    demo = GridDemo()
    demo.show()
    sys.exit(app.exec_())

main()