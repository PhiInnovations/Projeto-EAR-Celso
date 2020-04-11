from PyQt5.QtWidgets import QMainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import logging
from MainWindowUi import Ui_MainWindow

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
        self.btnUpdateSerialList.clicked.connect(self.updateSerialList)
        self.btnCommConnect.clicked.connect(self.connectSerial)
        self.comm.start()

        #
        # Initialize log file
        #
        self.file = None

        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

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

    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)

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
            return
        elif varName == 'EA':
            # Arm sensor position error count
            return
        elif varName == 'PW':
            # PWM Duty
            return
        elif varName == 'PS':
            # Px sensor
            return
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
