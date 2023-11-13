#!/usr/bin/python3
import sys
from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from datetime import datetime
import cv2
import numpy as np
from PIL import Image
import os
import face_recognition
import time

directory = "/home/pi/Desktop/"
path = directory+'dataset'
face_detector = cv2.CascadeClassifier(directory+'haarcascade_frontalface_default.xml')

class DoThreading(QThread):
    def __init__(self, _func):
        self.func = _func
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        self.func()

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        try:self.close()
        except: pass
        super(MyWindow, self).__init__()
        self.process_this_frame = True
        self.face_locations = []
        self.face_encodings = []
        self.faces_names = []
        self.faceSamples = []
        self.ids = []
        self.startTraining = False
        self.count = 0
        self.people = 0
        self.listOfPeople = []
        self.isUsing = False
        self.ids = []
        try: self.stop_webcamtrainer()
        except: pass
        self.people = 0
        self.listOfPeople = []
        f = open(directory+"DATABASE.txt", "r") #Read
        for x in f.readlines():
            self.listOfPeople.append(x.strip().split(",")[0])
        f.close()
        f = open(directory+"ENCODINGS.txt", "r")
        for x in f.readlines():
            if x != '':
                self.faceSamples.append(np.array(eval(x.split('=')[1])))
                self.ids.append(int(x.split('=')[0]))
        f.close()
        print(self.listOfPeople)
        self.counter = 1000
        try: self.out.release()
        except: pass
        self.start_webcam();

    def trainView(self):
        try:self.close()
        except: pass
        super(MyWindow, self).__init__()
        uic.loadUi(directory + 'TrainView.ui', self)
        self.setFixedSize(self.size())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.center()
        self.show()
        self.label_success.hide()
        self.pushButton.clicked.connect(self.doTraining)
        self.pushButton_2.clicked.connect(self.__init__)
        self.pushButton_3.clicked.connect(self.reset)
        self.start_webcamtrainer()

    def doTraining(self):
        if str(self.textEdit.toPlainText()) != "":
            self.startTraining = True
            self.people = 0
            self.listOfPeople = []
            f = open(directory+"DATABASE.txt", "r") #Read
            for x in f.readlines():
                self.listOfPeople.append(x.strip().split(",")[0])
                self.people = self.people + 1
            f.close()
        else:
            self.label_success.setText("SOME FIELDS ARE EMPTY!")
            self.label_success.show()
        
    def mapView(self):
        try:self.close()
        except: pass
        super(MyWindow, self).__init__()
        uic.loadUi(directory + 'MapView.ui', self)
        self.setFixedSize(self.size())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.center()
        self.show()
        self.pushButton.clicked.connect(self.__init__)

    ##WEBCAMTRAINER
    def start_webcamtrainer(self):
        self.capturetrain = cv2.VideoCapture(0)
        self.timertrain=QTimer(self)
        self.timertrain.timeout.connect(self.update_frametrainer)
        self.timertrain.start()

    def update_frametrainer(self):
        ret1, self.imagetrain = self.capturetrain.read()
        self.imagetrain=cv2.flip(self.imagetrain, 1)
        self.displayImageTrain(self.imagetrain, 1, "label")

    def stop_webcamtrainer(self):
        self.timertrain.stop()
        self.capturetrain.release()

    def __draw_label(self,img, text, pos, bg_color):
        font_face = cv2.FONT_HERSHEY_DUPLEX
        scale = 1
        color = (255, 255, 255)
        thickness = cv2.FILLED
        margin = 2

        txt_size = cv2.getTextSize(text, font_face, scale, thickness)

        end_x = pos[0] + txt_size[0][0] + margin
        end_y = pos[1] - txt_size[0][1] - margin

        cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
        cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

    def start_webcam(self):
        video_capture = cv2.VideoCapture(0)
        while True: #if window opened
            ret, img = video_capture.read()
            img = cv2.flip(img, 1)
            small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
            small_frame = small_frame[:, :, ::-1]
            now = datetime.now()
            dt_string = now.strftime("%m-%d-%Y %H.%M.%S")
            dt_string1 = now.strftime("%m-%d-%Y %H:%M:%S")
            self.__draw_label(img, dt_string1, (0,479), (0,0,255))
            img1 = img
            self.face_names = []
            if len(self.listOfPeople) != 0 and self.isUsing == False:
                if self.process_this_frame:
                    self.face_locations = face_recognition.face_locations(small_frame)
                    self.face_encodings = face_recognition.face_encodings(small_frame, self.face_locations)
                    for face_encoding in self.face_encodings:
                        matches = face_recognition.compare_faces(self.faceSamples, face_encoding, 0.4)
                        name = None

                        face_distances = face_recognition.face_distance(self.faceSamples, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            print(best_match_index)
                            name = self.listOfPeople[self.ids[best_match_index]-1]
                            self.face_names.append(name)
                self.process_this_frame = not self.process_this_frame
                for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    if self.isUsing == False and name != "unknown":
                        self.counter = 0
                        self.isUsing = True
                        self.dateToday = now.strftime("%m-%d-%Y")
                        self.timeCaught = now.strftime("%H:%M:%S")
                        self.theName = str(name)
                        print("CAPTURED "+self.theName)
                        self.__draw_label(img, 'CAPTURED '+self.theName, (0,22), (0,0,255))
                        cv2.imwrite(directory+"captured/"+self.theName+"("+str(dt_string)+").jpg", img1[top:bottom,left:right])
                        self.fourcc = cv2.VideoWriter_fourcc(*'XVID') #create a videowriter
                        self.out = cv2.VideoWriter(directory+'recorded/'+self.theName+"("+str(dt_string)+")"+'.avi',self.fourcc, 10.0, (640,480))
                        location = "Basement Entrance"
                        f = open(directory+"logs/"+self.dateToday+".txt","a+")
                        f.write(self.timeCaught+" "+self.theName+" was spotted at the "+location+"\n")
                        f.close()
            if cv2.waitKey(1) & 0xFF == ord('t'):
                self.key = 't'
                break
            if cv2.waitKey(1) & 0xFF == ord('m'):
                self.key = 'm'
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.key = 'q'
                break
            if self.isUsing == True:
                self.counter = self.counter + 1
                print("Recording: "+str(self.counter) + " Frames")
                if self.counter < 100:
                    self.__draw_label(img, 'RECORDING '+str(self.theName).upper(), (0,22), (0,0,255))
                    self.out.write(img)
                else:
                    self.counter = 0
                    self.out.release() #stopVideotra
                    self.isUsing = False
            cv2.namedWindow("SMART CCTV", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("SMART CCTV",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow('SMART CCTV', img)
        video_capture.release()
        cv2.destroyAllWindows()
        if self.key == 't':
            self.trainView()
        elif self.key == 'm':
            self.mapView()

    def encodingFaces(self, path, theID):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        self.faceSamples=[]
        self.ids = []
        if (len(imagePaths) != 0 or self.startTraining == True):
            for imagePath in imagePaths:
                id = int(os.path.split(imagePath)[-1].split(".")[1])
                if id == theID:
                    print(imagePath)
                    print(id)
                    imageFace = face_recognition.load_image_file(imagePath)
                    imageEncoding = face_recognition.face_encodings(imageFace)[0]
                    f = open(directory+"ENCODINGS.txt","a+")
                    f.write(str(id)+"="+str(imageEncoding.tolist())+"\n")
                    f.close()

    def displayImageTrain(self, img, window=1, labelName=""):
        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert image to grayscale
        if window == 1: #if window opened
            faces = face_detector.detectMultiScale(gray, 1.2, 1)
            for (x,y,w,h) in faces:
                if self.startTraining == True:    
                    self.count += 1
                    # Save the captured image into the datasets folder
                    cv2.imwrite(directory+"dataset/User." + str(self.people+1) + '.' + str(self.count) + ".jpg", img[y-20:y+h+10,x-2:x+w+4])
                    print("Working: "+str(self.count))
                cv2.rectangle(img, (x-2,y-20), (x+w+4,y+h+10), (255,0,0), 1)
                if self.count >= 3:
                    if str(self.textEdit.toPlainText()) != "":
                        f = open(directory+"DATABASE.txt","a+")
                        f.write(str(self.textEdit.toPlainText())+","+str(self.people+1)+"\n")
                        f.close()
                    self.encodingFaces(path, self.people+1)
                    self.people = 0
                    self.startTraining = False
                    if self.count == 3:
                        self.count = 0
                        self.label_success.setText("TRAINED SUCCESSFUL!")
                        self.label_success.show()
            self.outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888) #convert image to QImage
            self.outImage = self.outImage.rgbSwapped()
            lbl = self.findChild(QtGui.QLabel, labelName)
            lbl.setPixmap(QPixmap.fromImage(self.outImage)) #show the live image on the Graphical User Interface (GUI)

    def reset(self):
        open(directory+'DATABASE.txt', 'w').close()
        open(directory+'ENCODINGS.txt', 'w').close()
        for the_file in os.listdir(path):
            file_path = os.path.join(path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        for the_file in os.listdir(directory+"captured"):
            file_path = os.path.join(directory+"captured", the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        for the_file in os.listdir(directory+"recorded"):
            file_path = os.path.join(directory+"recorded", the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        for the_file in os.listdir(directory+"logs"):
            file_path = os.path.join(directory+"logs", the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        self.label_success.setText("RESET SUCCESSFUL!")
        self.label_success.show()

    #TOOLBOX    
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        
    def doMessage(self, text, caption="Info"):
        msg = QMessageBox(self)
        msg.setText(text)
        msg.setWindowTitle(caption)
        msg.show()
        return msg
    
    def doQuestion(self, text, caption):
        return QMessageBox.question(self, caption, text, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
