import sys
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QDesktopWidget
import threading
from pynput.mouse import Button,Controller
from pynput.keyboard import Controller as KController
from pynput.keyboard import Key
import time
import struct
import pyaudio
import pvporcupine
mouse = Controller()
keyboard=KController()
w=0
h=0
flag = True

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
        self.setWindowOpacity(0.60)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        ab = QDesktopWidget().screenGeometry()
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        global w
        global h
        w=int(width)
        h=int(height)
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
        values = ['Left-Click', 'No-Click', 'Hover', 'Double-Click', '', 'Right-Click', 'Scroll', 'On-Screen Keyboard', 'Drag']
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
        global flag
        sender = self.sender()
        if sender.text() == "Left-Click":
            self.close()
            self.win = Window('Left-Click Mode')
            flag = False
            time.sleep(0.3)
            flag = True
            left = threading.Thread(target=left_click, daemon=True)
            left.start()
        elif sender.text() == "No-Click":
            self.close()
            self.win = Window('No-Click Mode')
            flag = False
            time.sleep(0.3)
            flag = True
            nc = threading.Thread(target=no_click, daemon=True)
            nc.start()
        elif sender.text() == "On-Screen Keyboard":
            self.close()
            with keyboard.pressed(Key.cmd):
                with keyboard.pressed(Key.ctrl):
                    keyboard.press('o')
                    keyboard.release('o')
        elif sender.text() == "Hover":
            self.close()
            self.win = Window('Hover Mode')
            flag = False
            time.sleep(0.3)
            flag = True
            hr = threading.Thread(target=hover, daemon=True)
            hr.start()
        elif sender.text() == "Double-Click":
            self.close()
            self.win = Window('Double-Click Mode')
            flag = False
            time.sleep(0.3)
            flag = True
            dc = threading.Thread(target=double_click, daemon=True)
            dc.start()
        elif sender.text() == "Right-Click":
            self.close()
            self.win = Window('Right-Click Mode')
            flag = False
            time.sleep(0.3)
            flag = True
            right = threading.Thread(target=right_click, daemon=True)
            right.start()
        elif sender.text() == "Scroll":
            self.close()
            self.win = Window('Scroll Mode')
            flag = False
            time.sleep(0.3)
            flag = True
            sc = threading.Thread(target=scroll, daemon=True)
            sc.start()
        elif sender.text() == "Drag":
            self.close()
            self.win = Window('Drag Mode')
            flag = False
            time.sleep(0.3)
            flag = True
            dr = threading.Thread(target=drag, daemon=True)
            dr.start()
    def center(self):
        ab = QDesktopWidget().screenGeometry()
        w = ab.width()*0.3
        h = ab.height()*0.3
        self.resize(w,h)
        x = 0.5*w
        y = 0.5*h
        self.move((ab.width()/2)-x,(ab.height()/2)-y)
def no_click():
    while True:
        global flag
        if(flag==False):
            print("Exited no click")
            break
        time.sleep(0.25)
def left_click():
    print("left click")
    prevx = -1
    prevy = -1
    count=0
    while True:
        global flag
        if(flag==False):
            print("Exited left click")
            break
        #print("Entered loop")
        x,y=mouse.position
        #print("("+str(x)+","+str(y)+")")
        if (x<=prevx+5 and x>=prevx-5 and y<=prevy+5 and y>=prevy-5):
            count=count+1
            if(count>=3):
                mouse.click(Button.left)
                print("Mouse clicked")
                count=0
        else:
            count=0
        prevx=x
        prevy=y
        time.sleep(0.25)
def right_click():
    print("right click")
    prevx = -1
    prevy = -1
    count=0
    while True:
        global flag
        if (flag==False):
            print("Exited right click")
            break
        #print("Entered loop")
        x,y=mouse.position
        #print("("+str(x)+","+str(y)+")")
        if (x<=prevx+5 and x>=prevx-5 and y<=prevy+5 and y>=prevy-5):
            count=count+1
            if(count>=3):
                mouse.click(Button.right)
                print("Mouse clicked")
                count=0
        else:
            count=0
        prevx=x
        prevy=y
        time.sleep(0.25)
def double_click():
    prevx = -1
    prevy = -1
    count=0
    while True:
        global flag
        if (flag==False):
            print("Exited double click")
            break
        #print("Entered loop")
        x,y=mouse.position
        #print("("+str(x)+","+str(y)+")")
        if (x<=prevx+5 and x>=prevx-5 and y<=prevy+5 and y>=prevy-5):
            count=count+1
            if(count>=3):
                mouse.click(Button.left,2)
                print("Mouse clicked")
                count=0
        else:
            count=0
        prevx=x
        prevy=y
        time.sleep(0.25)
def hover():
    prevx = -1
    prevy = -1
    count=0
    while True:
        global flag
        if (flag==False):
            print("Exited hover mode")
            break
        #print("Entered loop")
        x,y=mouse.position
        #print("("+str(x)+","+str(y)+")")
        if (x<=prevx+5 and x>=prevx-5 and y<=prevy+5 and y>=prevy-5):
            count=count+1
            if(count>=8):
                mouse.click(Button.left)
                print("Mouse clicked")
                count=0
        else:
            count=0
        prevx=x
        prevy=y
        time.sleep(0.25)
def drag():
    prevx = -1
    prevy = -1
    count=0
    drag_on=0
    while True:
        global flag
        if (flag==False):
            print("Exited drag mode")
            break
        #print("Entered loop")
        x,y=mouse.position
        #print("("+str(x)+","+str(y)+")")
        if (x<=prevx+5 and x>=prevx-5 and y<=prevy+5 and y>=prevy-5):
            count=count+1
            if(count>=3):
                if(drag_on==0):
                    mouse.press(Button.left)
                else:
                    mouse.release(Button.left)
                drag_on=1-drag_on
                count=0
        else:
            count=0
        prevx=x
        prevy=y
        time.sleep(0.25)
def scroll():
    prevx = -1
    prevy = -1
    count=0
    while True:
        global flag
        if (flag==False):
            print("Exited scroll mode")
            break
        #print("Entered loop")
        x,y=mouse.position
        #print("("+str(x)+","+str(y)+")")
        if (x<=prevx+5 and x>=prevx-5 and y<=prevy+5 and y>=prevy-5):
            count=count+1
            if(count>=3):
                mouse.click(Button.middle)
                print("Mouse clicked")
                count=0
        else:
            count=0
        prevx=x
        prevy=y
        time.sleep(0.25)



def winCheck():
    global w
    global h
    while True:
        check = demo.isActiveWindow()
        #print("Active window : " + str(check))
        if (check):
            print(threading.active_count())
            xy = QDesktopWidget().screenGeometry()
            x=int(xy.width())
            y=int(xy.height())
            mouse.position = (int(x/2),int(y/2))
            global flag
            flag = False
            time.sleep(0.3)
            flag = True
            left = threading.Thread(target=left_click,daemon=True)
            left.start()
            while (demo.isActiveWindow()):
                time.sleep(1)

def wake(demo):

    porcupine = None
    pa = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(keywords=["computer"])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
                        rate=porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Hotword Detected")
                demo.show()
                demo.activateWindow()

    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
                pa.terminate()

if __name__ == "__main__":
    left = threading.Thread(target=left_click, daemon=True)
    left.start()
    app = QApplication(sys.argv)
    demo = GridDemo()
    demo.show()
    wc = threading.Thread(target=winCheck,daemon=True)
    wc.start()
    wk = threading.Thread(target=wake,daemon=True,args=(demo,))
    wk.start()
    sys.exit(app.exec_())

