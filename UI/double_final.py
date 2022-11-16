
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from numpy import loadtxt
import numpy as np
import pandas as pd
import pyqtgraph
from sig2 import *
import pandas as pd
import scipy.io as sio



class Remon(Ui_MainWindow):
    def __init__ (self, MainWindow):
        super(Remon, self).setupUi(MainWindow)
        self.flag = True
        self.scale = 50
        self.scale2 = 1
        self.scale3 = 1
        self.x1=[]
        self.y1=[]
        self.x = []
        self.y = []
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.data = []
        self.x13=[]
        self.y13=[]
        self.x3 = []
        self.y3 = []
        self.timer3 = QtCore.QTimer()
        self.timer3.setInterval(100)
        self.timer3.timeout.connect(self.update_plot_data3)
        self.data3 = []
        self.x12= []
        self.y12=[]
        self.x2 = []
        self.y2 = []
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(100)
        self.timer2.timeout.connect(self.update_plot_data2)
        self.data2 = []
        self.play1.clicked.connect(self.plotting)
        self.pause1.clicked.connect(self.StopTim)
        self.stop1.clicked.connect(self.CLR)
        self.play2.clicked.connect(self.plotting2)
        self.pause2.clicked.connect(self.StopTim2)
        self.stop2.clicked.connect(self.CLR2)
        self.clear1.clicked.connect(self.showDialog)
        self.clear2.clicked.connect(self.showDialog2)
        self.play3.clicked.connect(self.plotting3)
        self.pause3.clicked.connect(self.StopTim3)
        self.stop3.clicked.connect(self.CLR3)
        self.clear3.clicked.connect(self.showDialog3)
        self.plus1.clicked.connect(self.minimize)
        self.min1.clicked.connect(self.zooming)
        self.plus2.clicked.connect(self.minimize2)
        self.min2.clicked.connect(self.zooming2)
        self.plus3.clicked.connect(self.minimize3)
        self.min3.clicked.connect(self.zooming3)
        print("fel fol")
    def TIMER(self):
        
        self.timer.start()
    
    def TIMER2(self):
        
        self.timer2.start()
    
    def TIMER3(self):
        
        self.timer3.start()
        
    def CLR(self):
        self.w1.plotItem.clear()
        self.counter = 0
        self.timer.stop()
    
    def CLR2(self):
        self.w2.plotItem.clear()
        self.counter2 = 0
        self.timer2.stop()

    def CLR3(self):
        self.w3.plotItem.clear()
        self.counter3 = 0
        self.timer3.stop()

    def update_plot_data(self): 
        self.x1=self.x[:self.counter]
        self.y1=self.y[:self.counter] 
        self.w1.plotItem.setXRange(max(self.x1,default=0)-self.scale,max(self.x1,default=0))
        self.w1.plotItem.setYRange(min(self.y1,default=0),max(self.y1,default= 0))
        self.counter +=10
        self.data_line.setData(self.x1, self.y1)
    
    def update_plot_data2(self): 
        self.x12=self.x2[:self.counter2]
        self.y12=self.y2[:self.counter2]
        self.w2.plotItem.setXRange(max(self.x12,default=0)-self.scale2,max(self.x12,default=0))
        self.w2.plotItem.setYRange(min(self.y12,default=0), max(self.y12,default= 0))
        self.counter2+=10
        self.data_line2.setData(self.x12, self.y12)
    
    def update_plot_data3(self): 
        self.x13=self.x3[:self.counter3]
        self.y13=self.y3[:self.counter3] 
        self.w3.plotItem.setXRange(max(self.x13,default=0)-self.scale3, max(self.x13,default=0))
        self.w3.plotItem.setYRange(min(self.y13,default=0), max(self.y13,default= 0))
        self.counter3+=10
        self.data_line3.setData(self.x13, self.y13)

    def plotting(self):
        if len(self.data):
            #self.w1.setBackground('w')
            pen1 = pyqtgraph.mkPen(color=(0,0, 255))
            self.data_line =  self.w1.plotItem.plot(self.x1,self.y1,pen=pen1)
            self.TIMER()
        else:
            self.showDialog()

    def plotting2(self):
        if len(self.data2):
            #self.w2.setBackground('w')
            pen2 = pyqtgraph.mkPen(color=(0,255, 0))
            self.data_line2 =  self.w2.plotItem.plot(self.x12,self.y12,pen=pen2)
            self.TIMER2()
        else:
            self.showDialog2()

    def plotting3(self):
        if len(self.data3):
            #self.w1.setBackground('w')
            pen3 = pyqtgraph.mkPen(color=(255,0, 0  ))
            self.data_line3 =  self.w3.plotItem.plot(self.x13,self.y13,pen=pen3)
            self.TIMER3()
        else:
            self.showDialog3()
    
    def StopTim(self):
        self.timer.stop() 
    
    def StopTim2(self):
        self.timer2.stop() 

    def StopTim3(self):
        self.timer3.stop()    

    def zooming(self):
        if(self.scale< 90):
         self.scale += 10
    
    def zooming2(self):
     if(self.scale2< 90):
         self.scale2 += 10  
    
    def zooming3(self):
     if(self.scale3< 90):
         self.scale3 += 10

    def minimize(self):
        if(self.scale > 10):
            self.scale -= 10 
    
    def minimize2(self):
        if(self.scale2 > 10):
            self.scale2 -= 10 
    
    def minimize3(self):
        if(self.scale3 > 10):
            self.scale3 -= 10 

    def showDialog(self):
        self.data=[]
        self.x=[]
        self.y=[]
        self.counter=0
        self.timer.stop()
        self.w1.plotItem.clear()
        fname = QFileDialog.getOpenFileName(None, 'Open file', 'C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP')
        if fname[0]:
            if fname[0].endswith('.txt'):
                    self.data = loadtxt(fname[0])
                    self.x = self.data[:,0]
                    self.y = self.data[:,2]
        
            elif fname[0].endswith('.csv'):
                self.data=pd.read_csv(fname[0])
                self.y = self.data.iloc[:,0].values
                #for i in range len()
                self.x = np.asarray(range(len(self.y)))

            elif fname[0].endswith('.mat'):
                self.data =sio.loadmat(fname[0])
                self.data=self.data['F']
                for i in range(len(self.data)) :
                    for j in range(len(self.data[i,:])): 
                        self.y.append(self.data[i,j])
                self.x = np.asarray(range(len(self.y)))    
            # elif fname[0].endswith('.wav'):
            #     self.data=wavfile.read(fname[0])
            #     self.data=self.data[1]
            #     print(self.data)
    
    def showDialog2(self):
        self.data2=[]
        self.x2=[]
        self.y2=[]
        self.counter2=0
        self.timer2.stop()
        self.w2.plotItem.clear()
        fname = QFileDialog.getOpenFileName(None, 'Open file', 'C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP')
        if fname[0]:
            if fname[0].endswith('.txt'):
                        self.data2 = loadtxt(fname[0])
                        self.x2 = self.data2[:,0]
                        self.y2 = self.data2[:,2]
            
            elif fname[0].endswith('.csv'):
                self.data2=pd.read_csv(fname[0])
                self.y2 = self.data2.iloc[:,0].values
                #for i in range len()
                self.x2 = np.asarray(range(len(self.y2)))
            elif fname[0].endswith('.mat'):
                self.data2 =sio.loadmat(fname[0])
                self.data2=self.data2['F']
                for i in range(len(self.data2)) :
                    for j in range(len(self.data2[i,:])): 
                        self.y2.append(self.data2[i,j])
                self.x2 = np.asarray(range(len(self.y2)))   
            # elif fname[0].endswith('.wav'):
            #     self.data=wavfile.read(fname[0])
            #     self.data=self.data[1]
            #     print(self.data)

    def showDialog3(self):
        self.data2=[]
        self.x3=[]
        self.y3=[]
        self.counter3=0
        self.timer3.stop()
        self.w3.plotItem.clear()
        fname = QFileDialog.getOpenFileName(None, 'Open file', 'C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP')
        if fname[0]:
            if fname[0].endswith('.txt'):
                        self.data3 = loadtxt(fname[0])
                        self.x3 = self.data3[:,0]
                        self.y3 = self.data3[:,2]
            
            elif fname[0].endswith('.csv'):
                self.data3=pd.read_csv(fname[0])
                self.y3 = self.data3.iloc[:,0].values
                #for i in range len()
                self.x3 = np.asarray(range(len(self.y3)))
            elif fname[0].endswith('.mat'):
                self.data3 =sio.loadmat(fname[0])
                self.data3=self.data3['F']
                for i in range(len(self.data3)) :
                    for j in range(len(self.data3[i,:])): 
                        self.y3.append(self.data3[i,j])
                self.x3 = np.asarray(range(len(self.y3)))   
            # elif fname[0].endswith('.wav'):
            #     self.data=wavfile.read(fname[0])
            #     self.data=self.data[1]
            #     print(self.data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Remon(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())