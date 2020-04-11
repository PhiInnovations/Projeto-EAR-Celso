from PyQt5 import QtWidgets
from MainWindow import MainWindow
import sys
import os
import logging

def main():
    #
    # Setup logging
    #
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    #
    # Initialize and start main window
    #
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':         
    main()

