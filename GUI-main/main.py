import sys
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMainWindow, QSizePolicy, QApplication, QDesktopWidget, QShortcut, QSizeGrip

class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.shortcut_open = QShortcut(QKeySequence('Ctrl+T'), self)
        self.shortcut_open.activated.connect(self.on_open)

    def on_open(self):
        #self.setGeometry(300,200,500,400)
        #self.setWindowOpacity(0.85)
        #self.resize(400,400)
        #self.showFullScreen()
        #QWidget.showMaximized(self)
        ###  Here code for Directly shifting to Left-Click Mode now (i.e, on opening this window, auto-shift of mode)
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

class Window(QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText('Left-Click Mode')
        label.setFont(QtGui.QFont('Arial', 20))
        label.adjustSize()
        label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setStyleSheet("color:black; background-color: white;") #BG:#F5FFFA; #E3E3E3 - LightGray; white; #FFFF66 - LightYellow
        self.setWindowOpacity(0.80)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.show()         # Only after this, will frameGeometry() return actual dimensions
        ab = QDesktopWidget().screenGeometry()
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        #self.move((ab.width()-width), 100)         # Top Right Positioning

        dw = app.desktop()  # dw = QDesktopWidget() also works if app is created
        t_h = dw.screenGeometry().height() - dw.availableGeometry().height()
        self.move(ab.width()-width, dw.screenGeometry().height()-t_h-height)     # Bottom Right Positioning; For PPT Slideshow icons we can maybe even subtract some extra 20 from this statement height

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    demo = GridDemo()
    demo.show()
    sys.exit(app.exec_())