
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
        self.x1=[]
        self.y1=[]
        self.x = []
        self.y = []
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.data = []
        self.play1.clicked.connect(self.plotting)
        self.pause1.clicked.connect(self.StopTim)
        self.stop1.clicked.connect(self.CLR)
        # self.actionOpen.triggered.connect(self.showDialog)
    def TIMER(self):
        
        self.timer.start()
        
    def CLR(self):
        self.w1.plotItem.clear()
        self.counter = 0

    def update_plot_data(self): 
        self.x1=self.x[:self.counter]
        self.y1=self.y[:self.counter] 
        self.w1.plotItem.setXRange(min(self.x1,default=0),max(self.x1,default= 0))
        self.w1.plotItem.setYRange(min(self.y1,default=0),max(self.y1,default= 0))
        self.counter+=10
        self.data_line.setData(self.x1, self.y1)
    def plotting(self):
        if len(self.data):
            self.w1.setBackground('w')
            pen1 = pyqtgraph.mkPen(color=(0,0, 255))
            # x_axis=[2000]
            # y_axis=[1000]
            # self.w1.plot(x_axis,y_axis)
            self.data_line =  self.w1.plotItem.plot(self.x1,self.y1,pen=pen1)
            self.TIMER()
        else:
            self.showDialog()
    def StopTim(self):
        self.timer.stop()    
    def showDialog(self):
      fname = QFileDialog.getOpenFileName(None, 'Open file', '/Desktop')
      if fname[0]:    
        if fname[0].endswith('.txt'):
            self.data = loadtxt(fname[0])
            self.x = self.data[:,0]
            self.y = self.data[:,2]
            print(self.data)
            print(type(self.data))
        
        elif fname[0].endswith('.csv'):
            self.data=pd.read_csv(fname[0])
            self.y = self.data.iloc[:,0].values
            #for i in range len()
            self.x = np.asarray(range(len(self.y)))
            print(self.y)
            print(type(self.y))
            print(type(self.x))
            
        elif fname[0].endswith('.mat'):
            self.data =sio.loadmat(fname[0])
            self.data=self.data['F']
            for i in range(len(self.data)) :
                for j in range(len(self.data[i,:])): 
                    self.y.append(self.data[i,j])
            self.x = np.asarray(range(len(self.y))) 
                 

        elif fname[0].endswith('.wav'):
            self.data=wavfile.read(fname[0])
            self.data=self.data[1]
            print(self.data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Remon(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())