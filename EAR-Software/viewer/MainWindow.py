from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
import time
import logging
from MainWindowUi import Ui_MainWindow
from Comm import Comm

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        # Call the inherited classes __init__ method
        super(MainWindow, self).__init__()

        #
        # Setup UI components and fixed windows size
        #
        self.setupUi(self)

        #
        # Initializing communication and setup comm port
        # initialization buttons
        # Starting comm thread 
        #
        self.comm = Comm(callback=self.on_newMessage)
        self.btnUpdate.clicked.connect(self.updateSerialList)
        self.btnConnect.clicked.connect(self.connectSerial)
        self.btnLoadFile.clicked.connect(self.runFile)
        self.btnOpenFile.clicked.connect(self.getFile)
        self.comm.start()

        #
        # Initialize log file
        #
        self.file = None

        #
        # Initialize the plot structure
        # AS and PS curves
        #
        self.bufferSize = 100
        self.dataAS = np.zeros(self.bufferSize)
        self.curveAS = self.plotAS.plot()
        self.lineAS = self.plotAS.addLine(x=0)
        self.iAS = 0
        self.dataPS = np.zeros(self.bufferSize)
        self.curvePS = self.plotPS.plot()
        self.linePS = self.plotPS.addLine(x=0)
        self.iPS = 0
        #
        # Initialize bar graphs
        #
        self.prepareBarTV()

    def prepareBarTV(self):
        self.wTV = self.barGraphTV.addPlot()
        x = [ 0 ]
        y1 = [ 0 ]
        self.bgTV = pg.BarGraphItem(x=x, height=y1, width=0.5, brush='r')
        
        self.wTV.addItem(self.bgTV)
        self.wTV.hideAxis('bottom')
        self.wTV.hideAxis('left')

    def updateBarTV(self,value):
        self.bgTV.setOpts(height=value)
    
    def getFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"Dat Files", "","Cert Files (*.dat);;All Files (*)", options=options)
        if fileName:
            self.txtFile.setText(fileName)

    def runFile(self):
        filename = self.txtFile.text()
        try:
            with open(filename) as fp:
                line = fp.readline()
                self.on_newMessage(line)
                time.sleep(1)
                while line:
                    line = fp.readline()
                    self.on_newMessage(line)
                    time.sleep(1)
            self.statusbar.showMessage("File load successfully")
        except:
            self.statusbar.showMessage("Error during file operation")
            fp.close()

    def updateSerialList(self):
        if self.comm is not None:
            _list = self.comm.getComPorts()
            if len(_list) == 0:
                QMessageBox.warning(self,"Warning","Empty COM port list")
                logging.warning("Empty list")
            else:
                self.cbPorts.clear()
                for _com in _list:
                    logging.error("Empty list")
                    self.cbPorts.addItem(_com)
        else:
            QMessageBox.warning(self,"Warning","Error with comm instance")

    def connectSerial(self):
        if self.comm is not None:
            if self.comm.isOpen() == False:
                # Get the port from the combo box
                _port = str(self.cbPorts.currentText())
                logging.debug("Opening port %s at 115200 bps",_port)

                if self.comm.openPort(_port,115200) == True:
                    # Change the icon
                    icon5 = QtGui.QIcon()
                    icon5.addPixmap(QtGui.QPixmap(":/button/open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.btnCommConnect.setIcon(icon5)
                    self.btnCommConnect.setIconSize(QtCore.QSize(24, 24))
                    # Change the led
                    self.lblCommStatus.setPixmap(QtGui.QPixmap(":/leds/green"))
                    # Open file for logging received message
                    if self.file is not None:
                        self.file.close()
                    now = datetime.now()
                    ts = now.strftime("%Y%m%d%H%M%S")
                    msgFileName = "msgs_" + ts + ".dat"
                    try:
                        self.file = open(msgFileName,"w")
                    except:
                        self.statusbar.showMessage("Error opening data.")
                        self.file = None
                        return
                else:
                    QMessageBox.warning(self,"Warning","Error opening serial port")
            else:
                self.comm.closePort()
                # Change the icon
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap(":/button/close"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btnCommConnect.setIcon(icon5)
                self.btnCommConnect.setIconSize(QtCore.QSize(24, 24))
                # Change the led
                self.lblCommStatus.setPixmap(QtGui.QPixmap(":/leds/red"))
                #
                # Close the file
                #
                if self.file is not None:
                    self.file.close()
                    self.file = None
        else:
            QMessageBox.warning(self,"Warning","Error with comm instance")

    def plotPSCurve(self, value):
        #
        # Check if it arrived at the end of the plot
        # In this case, the buffer must be shifted to plot
        # the last value
        #
        if self.iPS == self.bufferSize:
            self.dataPS = np.roll(self.dataPS,-1)
            self.dataPS[self.iPS-1] = value
        else:
            self.dataPS[self.iPS] = value
            self.iPS = self.iPS + 1
        self.curvePS.setData(self.dataPS)
        pg.QtGui.QApplication.processEvents()

    def plotASCurve(self, value):
        #
        # Check if it arrived at the end of the plot
        # In this case, the buffer must be shifted to plot
        # the last value
        #
        if self.iAS == self.bufferSize:
            self.dataAS = np.roll(self.dataAS,-1)
            self.dataAS[self.iAS-1] = value
        else:
            self.dataAS[self.iAS] = value
            self.iAS = self.iAS + 1
        self.curveAS.setData(self.dataAS)
        pg.QtGui.QApplication.processEvents()

    def on_newMessage(self,message):
        #
        # Save the received message to the file
        #
        if self.file is not None:
            self.file.write(message)
        #
        # Separate the message content into variables
        #
        vars = message.strip().split(' ')
        #
        # sanity check
        #
        if len(vars) == 0:
            self.statusbar.showMessage("Invalid message received")
            return
        #
        # Process the message
        #
        isValid = False
        for idx, var in enumerate(vars):
            #
            # Check if it is a valid data
            #
            if idx == 0 and var == 'D':
                isValid = True
                continue
            #
            # Analyse in case of valid data
            #
            if isValid == True:
                #
                # Extract the content of the variable
                # and present it on the screen
                #
                self.extractShow(var)

    def extractShow(self,variable):
        content = variable.split(':')
        #
        # Sanity check
        #
        if len(content) != 2:
            self.statusbar.showMessage("Invalid variable: " + variable)
            return
        #
        # Identify the variable and show on the screen
        #
        varName = content[0]
        varValue = int(content[1])
        if varName == 'BC':
            # Breath Cycles
            return
        elif varName == 'MS':
            # Motor speed
            return
        elif varName == 'P1':
            # POT 1
            return
        elif varName == 'P2':
            # POT 2
            return
        elif varName == 'P3':
            # POT 3
            return
        elif varName == 'P4':
            # POT 4
            return
        elif varName == 'IM':
            # Motor current
            return
        elif varName == 'IP':
            # Motor Peak current
            return
        elif varName == 'AS':
            # Arm sensor position
            # Plot the value on a graph
            self.plotASCurve(varValue)
        elif varName == 'EA':
            # Arm sensor position error count
            return
        elif varName == 'PW':
            # PWM Duty
            return
        elif varName == 'PS':
            # Px sensor
            self.plotPSCurve(varValue)
        elif varName == 'PL':
            # Plateau pressure
            return
        elif varName == 'PM':
            # Pressure max limit
            return
        elif varName == 'AP':
            # Assisted pressure threshold
            return
        elif varName == 'TS':
            # Tidal volume enable
            return
        elif varName == 'BM':
            # BPM
            return
        elif varName == 'IE':
            # IE Ratio
            # 2 means 1:2
            # 3 means 1:3
            # ...
            return
        elif varName == 'TV':
            # Tidal volume
            return
        elif varName == 'PX':
            # Measured pressure
            return
        else:
            #
            # Unknown
            #
            self.statusbar.showMessage("Unknown variable name " + varName)
