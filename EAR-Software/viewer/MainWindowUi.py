# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 893)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plotAS = PlotWidget(self.centralwidget)
        self.plotAS.setGeometry(QtCore.QRect(10, 140, 781, 141))
        self.plotAS.setAutoFillBackground(True)
        self.plotAS.setObjectName("plotAS")
        self.cbPorts = QtWidgets.QComboBox(self.centralwidget)
        self.cbPorts.setGeometry(QtCore.QRect(80, 30, 101, 31))
        self.cbPorts.setObjectName("cbPorts")
        self.lblLed = QtWidgets.QLabel(self.centralwidget)
        self.lblLed.setGeometry(QtCore.QRect(20, 25, 41, 41))
        self.lblLed.setText("")
        self.lblLed.setPixmap(QtGui.QPixmap(":/leds/red"))
        self.lblLed.setScaledContents(True)
        self.lblLed.setObjectName("lblLed")
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setGeometry(QtCore.QRect(190, 30, 31, 31))
        self.btnConnect.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/button/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConnect.setIcon(icon)
        self.btnConnect.setIconSize(QtCore.QSize(24, 24))
        self.btnConnect.setObjectName("btnConnect")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(230, 30, 31, 28))
        self.btnUpdate.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/update"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate.setIcon(icon1)
        self.btnUpdate.setIconSize(QtCore.QSize(24, 24))
        self.btnUpdate.setObjectName("btnUpdate")
        self.lblMessage = QtWidgets.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(20, 80, 761, 41))
        self.lblMessage.setFrameShape(QtWidgets.QFrame.Box)
        self.lblMessage.setText("")
        self.lblMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessage.setObjectName("lblMessage")
        self.plotPS = PlotWidget(self.centralwidget)
        self.plotPS.setGeometry(QtCore.QRect(10, 300, 781, 141))
        self.plotPS.setAutoFillBackground(True)
        self.plotPS.setObjectName("plotPS")
        self.barGraphTV = GraphicsLayoutWidget(self.centralwidget)
        self.barGraphTV.setGeometry(QtCore.QRect(10, 460, 181, 191))
        self.barGraphTV.setAutoFillBackground(True)
        self.barGraphTV.setObjectName("barGraphTV")
        self.barGraphPX = GraphicsLayoutWidget(self.centralwidget)
        self.barGraphPX.setGeometry(QtCore.QRect(400, 460, 181, 191))
        self.barGraphPX.setAutoFillBackground(True)
        self.barGraphPX.setObjectName("barGraphPX")
        self.pot1 = QtWidgets.QDial(self.centralwidget)
        self.pot1.setGeometry(QtCore.QRect(130, 740, 91, 101))
        self.pot1.setObjectName("pot1")
        self.lblIE = QtWidgets.QLabel(self.centralwidget)
        self.lblIE.setGeometry(QtCore.QRect(250, 460, 111, 41))
        self.lblIE.setFrameShape(QtWidgets.QFrame.Box)
        self.lblIE.setText("")
        self.lblIE.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIE.setObjectName("lblIE")
        self.pot2 = QtWidgets.QDial(self.centralwidget)
        self.pot2.setGeometry(QtCore.QRect(260, 740, 91, 101))
        self.pot2.setObjectName("pot2")
        self.pot3 = QtWidgets.QDial(self.centralwidget)
        self.pot3.setGeometry(QtCore.QRect(390, 740, 91, 101))
        self.pot3.setObjectName("pot3")
        self.pot4 = QtWidgets.QDial(self.centralwidget)
        self.pot4.setGeometry(QtCore.QRect(520, 740, 91, 101))
        self.pot4.setObjectName("pot4")
        self.lblTS = QtWidgets.QLabel(self.centralwidget)
        self.lblTS.setGeometry(QtCore.QRect(120, 680, 91, 41))
        self.lblTS.setFrameShape(QtWidgets.QFrame.Box)
        self.lblTS.setText("")
        self.lblTS.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTS.setObjectName("lblTS")
        self.lblBM = QtWidgets.QLabel(self.centralwidget)
        self.lblBM.setGeometry(QtCore.QRect(260, 680, 91, 41))
        self.lblBM.setFrameShape(QtWidgets.QFrame.Box)
        self.lblBM.setText("")
        self.lblBM.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBM.setObjectName("lblBM")
        self.lblPM = QtWidgets.QLabel(self.centralwidget)
        self.lblPM.setGeometry(QtCore.QRect(400, 680, 91, 41))
        self.lblPM.setFrameShape(QtWidgets.QFrame.Box)
        self.lblPM.setText("")
        self.lblPM.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPM.setObjectName("lblPM")
        self.lblAP = QtWidgets.QLabel(self.centralwidget)
        self.lblAP.setGeometry(QtCore.QRect(540, 680, 91, 41))
        self.lblAP.setFrameShape(QtWidgets.QFrame.Box)
        self.lblAP.setText("")
        self.lblAP.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAP.setObjectName("lblAP")
        self.txtFile = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFile.setGeometry(QtCore.QRect(440, 30, 261, 31))
        self.txtFile.setObjectName("txtFile")
        self.btnOpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFile.setGeometry(QtCore.QRect(710, 30, 31, 28))
        self.btnOpenFile.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/file"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenFile.setIcon(icon2)
        self.btnOpenFile.setIconSize(QtCore.QSize(24, 24))
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.btnLoadFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadFile.setGeometry(QtCore.QRect(750, 30, 31, 28))
        self.btnLoadFile.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/button/play"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLoadFile.setIcon(icon3)
        self.btnLoadFile.setIconSize(QtCore.QSize(24, 24))
        self.btnLoadFile.setObjectName("btnLoadFile")
        self.barGraphAV = GraphicsLayoutWidget(self.centralwidget)
        self.barGraphAV.setGeometry(QtCore.QRect(600, 460, 181, 191))
        self.barGraphAV.setAutoFillBackground(True)
        self.barGraphAV.setObjectName("barGraphAV")
        self.lblPH = QtWidgets.QLabel(self.centralwidget)
        self.lblPH.setGeometry(QtCore.QRect(250, 510, 111, 41))
        self.lblPH.setFrameShape(QtWidgets.QFrame.Box)
        self.lblPH.setText("")
        self.lblPH.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPH.setObjectName("lblPH")
        self.lblEA = QtWidgets.QLabel(self.centralwidget)
        self.lblEA.setGeometry(QtCore.QRect(250, 560, 111, 41))
        self.lblEA.setFrameShape(QtWidgets.QFrame.Box)
        self.lblEA.setText("")
        self.lblEA.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEA.setObjectName("lblEA")
        self.lblEI = QtWidgets.QLabel(self.centralwidget)
        self.lblEI.setGeometry(QtCore.QRect(250, 610, 111, 41))
        self.lblEI.setFrameShape(QtWidgets.QFrame.Box)
        self.lblEI.setText("")
        self.lblEI.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEI.setObjectName("lblEI")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "e-AR Emergency Ventilator"))
from pyqtgraph import GraphicsLayoutWidget, PlotWidget
import resource_rc
