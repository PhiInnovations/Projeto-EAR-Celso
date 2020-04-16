import serial          
import json
import logging
import time
import asyncio
import sys

import serial.tools.list_ports

from PyQt5.QtCore import QThread

class Comm(QThread):
    """description of class"""

    TIMEOUT = 3

    def __init__(self,callback=None):
        QThread.__init__(self)
        #
        # Initialize serial instance
        #
        self.ser = serial.Serial()
        self.started = False
        self.callback = None
        #self.state = self.WAITING
        #
        # Setting the new message callback
        #
        self.callback = callback

    def getComPorts(self):
        ports = serial.tools.list_ports.comports()
        available_ports = []
        for p in ports:
            available_ports.append(p.device)

        logging.debug("Available com ports:")
        logging.debug(available_ports)

        return available_ports

    def openPort(self,port,baudrate):
        self.ser.port = port
        self.ser.baudrate = baudrate
        try:
            self.ser.open()
            #self.ser.timeout = self.TIMEOUT
            ret = self.ser.is_open
            if ret == True:
                logging.debug("Serial port open on %s (%d)",port,baudrate)
            else:
                logging.debug("Error opening serial port %s (%d)",port,baudrate)
            # Reset the reading state
            #self.state = self.WAITING
            return ret
        except:
            logging.error("Problem opening serial port")
            return False

    def closePort(self):
        if self.ser.is_open == True:
            self.ser.close()
            logging.debug("Serial port closed")

    def isOpen(self):
        return self.ser.is_open

    def sendCommand(self, message, callback):
        #
        # Adding STX and ETX to the message
        #
        _msg = '\x02' + message + '\x03'
        #
        # Setting the response callback
        #
        self.callback = callback
        #
        # Send the command through serial
        #
        self.ser.reset_input_buffer()
        self.ser.write(_msg.encode())
        logging.debug("Command sent: %s",message)

    def run(self):
        while True:
            if self.ser.is_open == True:
                # Get the byte
                try:
                    if self.ser.inWaiting() > 0:
                        msg = self.ser.readline().decode()
                        logging.debug("Received message: %s",msg)
                        if self.callback is not None:
                            self.callback(msg)
                except:
                    pass
            else:
                # Wait
                time.sleep(2)
