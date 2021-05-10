import sys
import urllib3
import requests
import urllib.request
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QDesktopWidget

Switch1 = 0
Switch2 = 0
Switch3 = 0

#This class represents the primary GUI window
class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.center()
        self.setWindowTitle("Assistive Suite")      
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        self.setStyleSheet("background-color: black")
        values = ['Switch 1','Switch 2','Switch 3']         #represents each button on GUI
        positions = [(r,c) for r in range(1) for c in range(3)]
        layout = QGridLayout()
        self.setLayout(layout)

        for positions, value in zip(positions, values):         #for each button in the grid,
            self.button = QPushButton(value)
            self.button.setStyleSheet("QPushButton{color:black; background-color : white; font-size: 17px; }QPushButton::pressed{background-color : #C0C0C0;}")
            self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout.addWidget(self.button, *positions)
            self.button.clicked.connect(self.btnClicked)        #if clicked, call btnClicked()

    #This function is used to bind actions to buttons on the grid when clicked
    def btnClicked(self):
        st = 0
        global Switch1
        global Switch2
        global Switch3
        sender = self.sender()
        if sender.text() == "Switch 1":         #to identify the clicked button
            print("hello")
            if(Switch1 == 0):
                print("hello")
                #weburl = http.request("GET","http://192.168.1.39/26/on")
                r = requests.get("http://192.168.1.39/26/on")
                st = int(r.status_code)
                print("hello")
            else:
                r = requests.get("http://192.168.1.39/26/off")
                st = int(r.status_code)
            if(st == 200):
                Switch1 = 1 - Switch1
        elif sender.text() == "Switch 2":
            print("hello")
            if(Switch2 == 0):
                print("hello")
                #weburl = http.request("GET","http://192.168.1.39/26/on")
                r = requests.get("http://192.168.1.39/27/on")
                st = int(r.status_code)
                print("hello")
            else:
                r = requests.get("http://192.168.1.39/27/off")
                st = int(r.status_code)
            if(st == 200):
                Switch2 = 1 - Switch2
        elif sender.text() == "Switch 3":
            print("hello")
            if(Switch3 == 0):
                print("hello")
                #weburl = http.request("GET","http://192.168.1.39/26/on")
                r = requests.get("http://192.168.1.39/14/on")
                st = int(r.status_code)
                print("hello")
            else:
                r = requests.get("http://192.168.1.39/14/off")
                st = int(r.status_code)
            if(st == 200):
                Switch3 = 1 - Switch3
                
    #This function is used to center the primary gui window 
    def center(self):
        ab = QDesktopWidget().screenGeometry()
        w = ab.width()*0.3
        h = ab.height()*0.3
        self.resize(w,h/2)
        x = 0.5*w
        y = 0.5*h
        self.move((ab.width()/2)-x,(ab.height()/2)-(y/2))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = GridDemo()       #instantiates the primary gui window
    demo.show()
    sys.exit(app.exec_())
