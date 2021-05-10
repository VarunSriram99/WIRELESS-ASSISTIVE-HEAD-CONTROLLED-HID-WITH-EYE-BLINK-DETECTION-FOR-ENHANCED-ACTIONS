import argparse
import cv2
import dlib
import imutils
import numpy as np
from imutils import face_utils
from imutils.video import FileVideoStream, VideoStream
from scipy.spatial import distance as dist

import sys
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication, QDesktopWidget
import threading
from pynput.mouse import Button,Controller
from pynput.keyboard import Controller as KController
from pynput.keyboard import Key
import time

mouse = Controller()        #for controlling mouse cursor
keyboard=KController()
w=0
h=0
flag = True         #to execute threads one at a time

#This function calculates EAR values
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

#This class represents the secondary status window
class Window(QWidget):
    def __init__(self, tt):
        super().__init__()
        self.setWindowTitle("Mode Window")
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        label = QtWidgets.QLabel(self)          #label represents window's text
        label.setText(tt)
        label.setFont(QtGui.QFont('Arial', 20))
        label.adjustSize()          #window size depends on text length
        label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)       #disables mouse events on window
        self.setStyleSheet("color:black; background-color: white;")
        self.setWindowOpacity(0.60)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()
        
        #To position the window above taskbar on the bottom right corner
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

        
#This class represents the primary GUI window
class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.win = Window('Left-Click Mode')        #instantiating the status window class
        self.center()
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.setWindowTitle("GUI Window")
        self.setWindowIcon(QtGui.QIcon("Python-symbol.jpg"))
        self.setStyleSheet("background-color: black")
        values = ['Left-Click', 'No-Click', 'Hover', 'Double-Click', '', 'Right-Click', 'Scroll', 'On-Screen Keyboard', 'Drag']     #represents each button on GUI
        positions = [(r, c) for r in range(4) for c in range(3)]
        layout = QGridLayout()
        self.setLayout(layout)
        for positions, value in zip(positions, values):     #for each button in the grid,
            self.button = QPushButton(value)
            self.button.setStyleSheet("QPushButton{color:black; background-color : white; font-size: 17px; }QPushButton::pressed{background-color : #C0C0C0;}")
            self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout.addWidget(self.button, *positions)
            self.button.clicked.connect(self.btnClicked)    #if clicked, call btnClicked()
    
    #This function is used to bind actions to buttons on the grid when clicked
    def btnClicked(self):
        global flag
        sender = self.sender()
        if sender.text() == "Left-Click":       #to identify the clicked button
            self.close()        #closes primary window
            self.win = Window('Left-Click Mode')
            flag = False        #stop execution of current thread
            time.sleep(0.3)
            flag = True
            left = threading.Thread(target=left_click, daemon=True)         #create a new thread for executing left_click()
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
            with keyboard.pressed(Key.cmd):         #to close the keyboard, if user clicks cmd+ctrl+o
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
    
    #This function is used to center the primary gui window
    def center(self):
        ab = QDesktopWidget().screenGeometry()
        w = ab.width()*0.3
        h = ab.height()*0.3
        self.resize(w,h)
        x = 0.5*w
        y = 0.5*h
        self.move((ab.width()/2)-x,(ab.height()/2)-y)
        
#This function performs no actions and runs till flag becomes false        
def no_click():
    while True:
        global flag
        if(flag==False):        #to stop execution when another mouse mode is selected
            print("Exited no click")
            break
        time.sleep(0.25)
        
#This function performs a left click action        
def left_click():
    print("left click")
    prevx = -1      #to detect cursor's deviations
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
        if (x<=prevx+5 and x>=prevx-5 and y<=prevy+5 and y>=prevy-5):       #if there is a considerable cursor movement
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
        
#This function performs a right click action        
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
        
#This function performs two consecutive left clicks         
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
        
#This function performs a left click with extended delay to hover        
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
        
#This function alternates between mouse press & release to perform a mouse drag        
def drag():
    prevx = -1
    prevy = -1
    count=0
    drag_on=0       #to alternate between mouse's press and release
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
        
#This function uses the mouse middle button to perform scrolling        
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


#This function centers the mouse cursor and selects left click mode each time the gui pops up
def winCheck():
    global w
    global h
    while True:
        check = demo.isActiveWindow()
        #print("Active window : " + str(check))
        if (check):         #if window is actively in foreground
            print(threading.active_count())
            xy = QDesktopWidget().screenGeometry()
            x=int(xy.width())
            y=int(xy.height())
            mouse.position = (int(x/2),int(y/2))        #centers the mouse cursor
            global flag
            flag = False
            time.sleep(0.3)
            flag = True
            left = threading.Thread(target=left_click,daemon=True)          #creates a thread for left click operation
            left.start()
            while (demo.isActiveWindow()):
                time.sleep(1)

def wake(demo):
    
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-p", "--shape-predictor", required=True, help="path to facial landmark predictor"
    )
    ap.add_argument("-v", "--video", type=str, default= "", help="path to input video file")
    args = vars(ap.parse_args())


    EYE_AR_THRESH = 0.24
    EYE_AR_CONSEC_FRAMES = 4


    COUNTER = 0
    COUNTERO= 0
    TOTAL = 0


    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(args["shape_predictor"])


    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


    print("[INFO] starting video stream thread...")
    vs = FileVideoStream(args["video"]).start()
    fileStream = True
    vs = VideoStream(src=0).start()
    fileStream = False
    time.sleep(1.0)


    while True:

        if fileStream and not vs.more():
            break

        frame = vs.read()
        frame = imutils.resize(frame, width=800)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)

        for rect in rects:

            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            ear = (leftEAR + rightEAR) / 2.0

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
            st=time.perf_counter()
           

           
                
            if ear < EYE_AR_THRESH:
                COUNTER += 1 #for eye open and close 
                

            else:
                COUNTERO += 1
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    TOTAL += 1
                    COUNTERO= 0
                if COUNTERO >=6 and TOTAL> 0 :
                    COUNTERO =0
                    TOTAL= 0
                
                COUNTER = 0
                
            
            if (TOTAL==2) :
                
                demo.show()
                demo.activateWindow()
                TOTAL=0       

            cv2.putText(
                frame,
                "Blinks: {}".format(TOTAL),
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
            )
            cv2.putText(
                frame,
                "EAR: {:.2f}".format(ear),
                (300, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
            )
          
            

            cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF  
        if key == ord("q"):
            break
            cv2.destroyAllWindows()
            vs.stop()

if __name__ == "__main__":
    left = threading.Thread(target=left_click, daemon=True)         #creates a thread for left click operation initially
    left.start()
    app = QApplication(sys.argv)
    demo = GridDemo()       #instantiates the primary gui window
    demo.show()
    wc = threading.Thread(target=winCheck,daemon=True)
    wc.start()
    wk = threading.Thread(target=wake,daemon=True,args=(demo,))
    wk.start()
    sys.exit(app.exec_())
    
    #--shape-predictor shape_predictor_68_face_landmarks.dat

