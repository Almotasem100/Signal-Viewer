
from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
# # Package used for loading data from the input text file
from numpy import loadtxt

class MainWindow(QtWidgets.QMainWindow):
    counter=0
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.data=loadtxt("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Project\\DSP\\texfil.txt")
        self.x=[]
        self.y=[]
        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        x_axis=[2000]
        y_axis=[1000]
        self.graphWidget.plot(x_axis,y_axis)
        self.data_line =  self.graphWidget.plot(self.x,self.y,pen=pen)
        # ... init continued ...
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        

    def update_plot_data(self):
        self.x=self.data[:self.counter,0]
        self.y=self.data[:self.counter,2] 
        self.counter+=10
        self.data_line.setData(self.x, self.y)  # Update the data.    

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())