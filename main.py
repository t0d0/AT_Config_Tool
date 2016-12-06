#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
"""myapp1.pyw: Create an instance of Ui_Form."""
# pylint: disable=no-name-in-module
import sys
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui import Ui_MainWindow
from ui_manager import *
from serial_manager import *
#import time


class MyApp(Ui_MainWindow):

    parse_triggered = pyqtSignal()

    def __init__(self, parent=None, name=None):
        Ui_MainWindow.__init__(self)

if __name__ == "__main__":
    jsonstr = open('.config').read()
    print(json.loads(jsonstr))
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    
    ui = MyApp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
#   UI_manager
    ui_m = MainUIManager(ui)
#   Serial_manager
    ser_m = SerialArduino()
    
#   Set serial_port to combo_box
    for i in ser_m.get_port_list():
      ui_m.add_port(i)

#   Set event when clicked send_button
    ui_m.set_send_action(lambda:ser_m.write_list(ui_m.get_parameters_to_list(),ui_m.get_selected_port()))

  
#   exit
    sys.exit(app.exec_())