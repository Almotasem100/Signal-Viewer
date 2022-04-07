

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    counter = 0
    counter2 = 0
    counter3 = 0
    def setupUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_channel = QtWidgets.QVBoxLayout()
        self.verticalLayout_channel.setObjectName("verticalLayout_channel")
        self.horizontalLayout__1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout__1.setObjectName("horizontalLayout__1")
        self.horizontalLayout__2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout__2.setObjectName("horizontalLayout__2")
        self.horizontalLayout__3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout__3.setObjectName("horizontalLayout__3")

        self.horizontalLayout.addLayout(self.verticalLayout_channel)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_5.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_5.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_5.addWidget(self.checkBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuHep = QtWidgets.QMenu(self.menubar)
        self.menuHep.setObjectName("menuHep")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        print(type(self._translate))
        MainWindow.setWindowTitle(self._translate("MainWindow", "Team_20 Signal Viewer"))
            
        self.checkBox_1.setText(self._translate("MainWindow", "Signal 1"))
        self.checkBox_1.stateChanged.connect(self.click_1)
        
        self.checkBox_2.setText(self._translate("MainWindow", "Signal 2"))
        self.checkBox_2.stateChanged.connect(self.click_2)
        
        self.checkBox_3.setText(self._translate("MainWindow", "Signal 3"))
        self.checkBox_3.stateChanged.connect(self.click_3)
        


    def click_1(self , state):
        if self.checkBox_1.isChecked() == True:
            self.w1 = PlotWidget(self.centralwidget)
            self.w1.setMinimumSize(QtCore.QSize(50, 50))
            self.w1.setObjectName("w1")
            self.horizontalLayout__1.addWidget(self.w1)
            self.VL_B1 = QtWidgets.QVBoxLayout()
            self.VL_B1.setObjectName("VL_B1")
            self.B1_1 = QtWidgets.QPushButton(self.centralwidget)
            self.B1_1.setObjectName("B1_1")
            self.VL_B1.addWidget(self.B1_1)
            self.B1_2 = QtWidgets.QPushButton(self.centralwidget)
            self.B1_2.setObjectName("B1_2")
            self.VL_B1.addWidget(self.B1_2)
            self.B1_3 = QtWidgets.QPushButton(self.centralwidget)
            self.B1_3.setObjectName("B1_3")
            self.VL_B1.addWidget(self.B1_3)
            self.B1_4 = QtWidgets.QPushButton(self.centralwidget)
            self.B1_4.setObjectName("B1_4")
            self.VL_B1.addWidget(self.B1_4)
            self.horizontalLayout__1.addLayout(self.VL_B1)
            self.verticalLayout_channel.addLayout(self.horizontalLayout__1)
            self.B1_1.setText(self._translate("MainWindow", "Play"))
            self.B1_2.setText(self._translate("MainWindow", "Pause"))
            self.B1_3.setText(self._translate("MainWindow", "Stop"))
            self.B1_4.setText(self._translate("MainWindow", "Open File"))
            self.B1_1.setIcon(QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\resume.png")) 
            self.B1_2.setIcon(QtGui.QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\stop.png")) 
            self.B1_3.setIcon(QtGui.QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\pause1.png"))
            self.B1_1.setIconSize(QtCore.QSize(25,25))
            self.B1_2.setIconSize(QtCore.QSize(25,25))
            self.B1_3.setIconSize(QtCore.QSize(25,25))

            
        else:

            self.VL_B1.removeWidget(self.B1_1)
            self.B1_1.deleteLater()
            self.B1_1 = None
            self.VL_B1.removeWidget(self.B1_2)
            self.B1_2.deleteLater()
            self.B1_2 = None
            self.VL_B1.removeWidget(self.B1_3)
            self.B1_3.deleteLater()
            self.B1_3 = None
            self.VL_B1.removeWidget(self.B1_4)
            self.B1_4.deleteLater()
            self.B1_4 = None
            self.horizontalLayout__1.removeWidget(self.w1)
            self.w1.deleteLater()
            self.w1 = None
            self.st_1 = False
    def click_2(self , state):
        if self.checkBox_2.isChecked() == True:
            print ("st_2 = True")
            self.w2 = PlotWidget(self.centralwidget)
            self.w2.setMinimumSize(QtCore.QSize(50, 50))
            self.w2.setObjectName("w2")
            self.horizontalLayout__2.addWidget(self.w2)
            self.verticalLayout_4 = QtWidgets.QVBoxLayout()
            self.verticalLayout_4.setObjectName("verticalLayout_4")
            self.B2_1 = QtWidgets.QPushButton(self.centralwidget)
            self.B2_1.setObjectName("B2_1")
            self.verticalLayout_4.addWidget(self.B2_1)
            self.B2_2 = QtWidgets.QPushButton(self.centralwidget)
            self.B2_2.setObjectName("B2_2")
            self.verticalLayout_4.addWidget(self.B2_2)
            self.B2_3 = QtWidgets.QPushButton(self.centralwidget)
            self.B2_3.setObjectName("B2_3")
            self.verticalLayout_4.addWidget(self.B2_3)
            self.B2_4 = QtWidgets.QPushButton(self.centralwidget)
            self.B2_4.setObjectName("B2_4")
            self.verticalLayout_4.addWidget(self.B2_4)
            self.horizontalLayout__2.addLayout(self.verticalLayout_4)
            self.verticalLayout_channel.addLayout(self.horizontalLayout__2)
            self.B2_1.setText(self._translate("MainWindow", "Play"))
            self.B2_2.setText(self._translate("MainWindow", "Pause"))
            self.B2_3.setText(self._translate("MainWindow", "Stop"))
            self.B2_4.setText(self._translate("MainWindow", "Open File"))
            self.B2_1.setIcon(QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\resume.png")) 
            self.B2_2.setIcon(QtGui.QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\stop.png")) 
            self.B2_3.setIcon(QtGui.QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\pause1.png"))
            self.B2_1.setIconSize(QtCore.QSize(25,25))
            self.B2_2.setIconSize(QtCore.QSize(25,25))
            self.B2_3.setIconSize(QtCore.QSize(25,25))
        else:
            
            self.verticalLayout_4.removeWidget(self.B2_1)
            self.B2_1.deleteLater()
            self.B2_1 = None
            self.verticalLayout_4.removeWidget(self.B2_2)
            self.B2_2.deleteLater()
            self.B2_2 = None
            self.verticalLayout_4.removeWidget(self.B2_3)
            self.B2_3.deleteLater()
            self.B2_3 = None
            self.verticalLayout_4.removeWidget(self.B2_4)
            self.B2_4.deleteLater()
            self.B2_4 = None
            self.horizontalLayout__2.removeWidget(self.w2)
            self.w2.deleteLater()
            self.w2 = None
            self.st_2 = False

    def click_3(self , state):
        if self.checkBox_3.isChecked() == True:
            
            self.w3 = PlotWidget(self.centralwidget)
            self.w3.setMinimumSize(QtCore.QSize(50, 50))
            self.w3.setObjectName("w3")
            self.horizontalLayout__3.addWidget(self.w3)
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setObjectName("verticalLayout")
            self.B3_1 = QtWidgets.QPushButton(self.centralwidget)
            self.B3_1.setObjectName("B3_1")
            self.verticalLayout.addWidget(self.B3_1)
            self.B3_2 = QtWidgets.QPushButton(self.centralwidget)
            self.B3_2.setObjectName("B3_2")
            self.verticalLayout.addWidget(self.B3_2)
            self.B3_3 = QtWidgets.QPushButton(self.centralwidget)
            self.B3_3.setObjectName("B3_3")
            self.verticalLayout.addWidget(self.B3_3)
            self.B3_4 = QtWidgets.QPushButton(self.centralwidget)
            self.B3_4.setObjectName("B3_4")
            self.verticalLayout.addWidget(self.B3_4)
            self.horizontalLayout__3.addLayout(self.verticalLayout)
            self.verticalLayout_channel.addLayout(self.horizontalLayout__3)
            self.B3_1.setText(self._translate("MainWindow", "Play"))
            self.B3_2.setText(self._translate("MainWindow", "Pause"))
            self.B3_3.setText(self._translate("MainWindow", "Stop"))
            self.B3_4.setText(self._translate("MainWindow", "Open File"))
            self.B3_1.setIcon(QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\resume.png")) 
            self.B3_2.setIcon(QtGui.QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\stop.png")) 
            self.B3_3.setIcon(QtGui.QIcon("C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Python\\DSP\\images\\pause1.png"))
            self.B3_1.setIconSize(QtCore.QSize(25,25))
            self.B3_2.setIconSize(QtCore.QSize(25,25))
            self.B3_3.setIconSize(QtCore.QSize(25,25))
        else:
            self.verticalLayout.removeWidget(self.B3_1)
            self.B3_1.deleteLater()
            self.B3_1 = None
            self.verticalLayout.removeWidget(self.B3_2)
            self.B3_2.deleteLater()
            self.B3_2 = None
            self.verticalLayout.removeWidget(self.B3_3)
            self.B3_3.deleteLater()
            self.B3_3 = None
            self.verticalLayout.removeWidget(self.B3_4)
            self.B3_4.deleteLater()
            self.B3_4 = None
            self.horizontalLayout__3.removeWidget(self.w3)
            self.w3.deleteLater()
            self.w3 = None
        
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
