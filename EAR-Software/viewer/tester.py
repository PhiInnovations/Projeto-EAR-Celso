import logging
import sys
import serial
import time
import signal

ser = serial.Serial()

def signal_handler(sig, frame):
    print("Finishing operation")
    ser.close()
    sys.exit(0)

def main():
    #
    # Setup logging
    #
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " <serialPort> <filename>")
        sys.exit(1)

    #
    # Capture parameters
    #
    logging.debug("Capturing information")
    serialPort = sys.argv[1]
    fileName = sys.argv[2]
    logging.debug("port %s file %s",serialPort,fileName)

    #
    # Open serial port
    #
    logging.debug("Opening serial port: " + serialPort)
    ser.port = serialPort
    ser.baudrate = 57600
    try:
        ser.open()
        #ser.timeout = self.TIMEOUT
        ret = ser.is_open
        if ret == True:
            print("Serial port open on {} ({})".format(serialPort,115200))
        else:
            print("Error opening serial port {} ({})".format(serialPort,115200))
            sys.exit(1)
    except Exception as e:
        logging.debug(e)
        print("Problem opening serial port")
        sys.exit(1)

    #
    # Open file and read lines
    #
    logging.debug("Reading file")
    try:
        fp = open(fileName,'r')
        Lines = fp.readlines()
    except Exception as e:
        logging.debug(e)
        print("Problem opening file")
        ser.close()
        sys.exit(1)

    #
    # Sending lines to the serial
    #
    logging.debug("Sending data")
    signal.signal(signal.SIGINT, signal_handler)
    try:
        while True:
            for line in Lines:
                ser.write(line.encode())
                time.sleep(0.1)
    except Exception as e:
        logging.debug(e)
        print("Problem sending data")
        ser.close()
        sys.exit(1)

if __name__ == '__main__':         
    main()

