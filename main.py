#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
"""myapp1.pyw: Create an instance of Ui_Form."""
# pylint: disable=no-name-in-module
import sys
#from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# pyuic5.bat myform.ui > ui_myform.py
#from ui_myform import Ui_Form
from ui import Ui_MainWindow

import sys
import time


class MyApp(Ui_MainWindow):

    parse_triggered = pyqtSignal()

    def __init__(self, parent=None, name=None):
        Ui_MainWindow.__init__(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MyApp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())