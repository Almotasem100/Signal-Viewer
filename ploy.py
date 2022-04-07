# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wiget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import loadtxt
import pyqtgraph


class Ui_MainWindow(object):
    counter=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.w1 = PlotWidget(self.centralwidget)
        self.w1.setGeometry(QtCore.QRect(10, 10, 771, 211))
        self.w1.setObjectName("w1")
        self.w2 = PlotWidget(self.centralwidget)
        self.w2.setGeometry(QtCore.QRect(10, 230, 771, 211))
        self.w2.setObjectName("w2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 500, 231, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 510, 231, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
from pyqtgraph import PlotWidget
class Remon(Ui_MainWindow):
    def __init__ (self, MainWindow):
        super(Remon, self).setupUi(MainWindow)
        self.x=[]
        self.y=[]
        #self.data = []
        self.pushButton.clicked.connect(self.plotting)
        self.pushButton_2.clicked.connect(self.StopTim)
        print("fel fol")
    def TIMER(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        
    def update_plot_data(self):
        self.x=self.data[:self.counter,0]
        self.y=self.data[:self.counter,2] 
        self.counter+=10
        self.data_line.setData(self.x, self.y)
    def plotting(self):
        self.data=loadtxt("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Project\\DSP\\texfil.txt")
        self.w1.setBackground('k')
        pen = pyqtgraph.mkPen(color=(255, 255, 255))
        x_axis=[2000]
        y_axis=[1000]
        self.w1.plot(x_axis,y_axis)
        self.data_line =  self.w1.plotItem.plot(self.x,self.y,pen=pen)
        self.TIMER()
    def StopTim(self):
        self.timer.stop()
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Remon(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
