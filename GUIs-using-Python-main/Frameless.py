import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QSizeGrip, QDesktopWidget
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText('Left-Click Mode')
        label.setFont(QtGui.QFont('Arial', 20))
        label.adjustSize()
        label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.setWindowTitle("Frameless")
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setStyleSheet("color:black; background-color: #F5FFFAFF;") #BG:#F5FFFA; #E3E3E3 - LightGray; white; #FFFF66 - LightYellow
        self.setWindowOpacity(0.85)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.show()         # Only after this, will frameGeometry() return actual dimensions
        ab = QDesktopWidget().screenGeometry()
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        #self.move((ab.width()-width), 0)         # Top Right Positioning

        dw = App.desktop()  # dw = QDesktopWidget() also works if app is created
        th = dw.screenGeometry().height() - dw.availableGeometry().height()
        self.move(ab.width()-width, ab.height()-th-height)     # Bottom Right Positioning; For PPT Slideshow icons we can maybe even subtract some extra 20 from this statement height

if __name__ == "__main__":
    App = QApplication(sys.argv)
    win = Window()
    sys.exit(App.exec_())