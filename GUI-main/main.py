import sys
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMainWindow, QSizePolicy, QApplication, QDesktopWidget, QShortcut, QSizeGrip


class Window(QWidget):
    def __init__(self, tt):
        super().__init__()
        self.setWindowTitle("Mode Window")
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        label = QtWidgets.QLabel(self)
        label.setText(tt)
        label.setFont(QtGui.QFont('Arial', 20))
        label.adjustSize()
        label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setStyleSheet("color:black; background-color: white;")
        self.setWindowOpacity(0.80)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        ab = QDesktopWidget().screenGeometry()
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        dw = app.desktop()
        t_h = dw.screenGeometry().height() - dw.availableGeometry().height()
        self.move(ab.width()-width, dw.screenGeometry().height()-t_h-height)


class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.win = Window('Left-Click Mode')
        self.center()
        self.setWindowTitle("GUI Window")
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        self.setStyleSheet("background-color: black")
        values = ['Left-Click', '', 'Hover', 'Middle-Click', '', 'Right-Click', 'Scroll', '', 'Drag']
        positions = [(r, c) for r in range(4) for c in range(3)]
        layout = QGridLayout()
        self.setLayout(layout)
        for positions, value in zip(positions, values):
            self.button = QPushButton(value)
            self.button.setStyleSheet("QPushButton{color:black; background-color : white; font-size: 17px; }QPushButton::pressed{background-color : #C0C0C0;}")
            self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout.addWidget(self.button, *positions)
            self.button.clicked.connect(self.btnClicked)
    def btnClicked(self):
        sender = self.sender()
        if sender.text() == "Left-Click":
            self.win = Window('Left-Click Mode')
            self.showMinimized()
        elif sender.text() == "Hover":
            self.win = Window('Hover Mode')
            self.showMinimized()
        elif sender.text() == "Middle-Click":
            self.win = Window('Middle-Click Mode')
            self.showMinimized()
        elif sender.text() == "Right-Click":
            self.win = Window('Right-Click Mode')
            self.showMinimized()
        elif sender.text() == "Scroll":
            self.win = Window('Scroll Mode')
            self.close()
        elif sender.text() == "Drag":
            self.win = Window('Drag Mode')
            self.close()
    def center(self):
        ab = QDesktopWidget().screenGeometry()
        w = ab.width()*0.3
        h = ab.height()*0.3
        self.resize(w,h)
        x = 0.5*w
        y = 0.5*h
        self.move((ab.width()/2)-x,(ab.height()/2)-y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = GridDemo()
    demo.show()
    sys.exit(app.exec_())
