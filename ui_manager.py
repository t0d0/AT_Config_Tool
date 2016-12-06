#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ui import Ui_MainWindow

class ImportUIManager():
  def __init__(self,import_window):
    pass

class ExportUIManager():
  def __init__(self,export_window):
    pass


class MainUIManager():

  def __init__(self,ui):
    self.obj_list = []
    self.ui = ui
    self.slider_init()

  
  def slider_init(self):
    self.slider_linker(self.ui.sl1,self.ui.sp1)
    self.slider_linker(self.ui.sl2,self.ui.sp2) 
    self.slider_linker(self.ui.sl3,self.ui.sp3)
    self.slider_linker(self.ui.sl4,self.ui.sp4)
    self.slider_linker(self.ui.sl5,self.ui.sp5)
    self.slider_linker(self.ui.sl6,self.ui.sp6)
    self.slider_linker(self.ui.sl7,self.ui.sp7)
    self.slider_linker(self.ui.sl8,self.ui.sp8)
    self.slider_linker(self.ui.sl9,self.ui.sp9)
    self.slider_linker(self.ui.sl10,self.ui.sp10)

  def set_by_list(self,datas):
    setters = [
      self.set_uphill_border,
      self.set_downhill_border,
      self.set_gear_steps,
      self.set_flat_accell_gear_up,
      self.set_flat_accell_gear_down,
      self.set_flat_cruise_gear_up,
      self.set_flat_cruise_gear_down,
      self.set_uphill_accell_gear_up,
      self.set_uphill_accell_gear_down,
      self.set_uphill_cruise_gear_up,
      self.set_uphill_cruise_gear_down,
      self.set_downhill_gear_up,
      self.set_downhill_gear_down,
      self.set_stop_speed,
      ]
    for (data,setter) in zip(datas,setters):
      setter(data)

  def get_parameters_to_list(self):
    ans = []
    getters = [
    self.get_uphill_border,
    self.get_downhill_border,
    self.get_gear_steps,
    self.get_flat_accell_gear_up,
    self.get_flat_accell_gear_down,
    self.get_flat_cruise_gear_up,
    self.get_flat_cruise_gear_down,
    self.get_uphill_accell_gear_up,
    self.get_uphill_accell_gear_down,
    self.get_uphill_cruise_gear_up,
    self.get_uphill_cruise_gear_down,
    self.get_downhill_gear_up,
    self.get_downhill_gear_down,
    self.get_stop_speed
    ]
    for getter in getters:
      ans.append(getter())
    return(ans)

  def slider_linker(self,slider,spiner):
    slider.valueChanged.connect(lambda :spiner.setValue(slider.value()))
    spiner.valueChanged.connect(lambda :slider.setValue(spiner.value()))


#  ----------Getter----------
  def get_flat_accell_gear_up(self):
    return(self.ui.sp1.value())
  
  def get_flat_accell_gear_down(self):
    return(self.ui.sp2.value())
  
  def get_flat_cruise_gear_up(self):
    return(self.ui.sp3.value())
  
  def get_flat_cruise_gear_down(self):
    return(self.ui.sp4.value())
  
  def get_uphill_accell_gear_up(self):
    return(self.ui.sp5.value())
  
  def get_uphill_accell_gear_down(self):
    return(self.ui.sp6.value())
  
  def get_uphill_cruise_gear_up(self):
    return(self.ui.sp7.value())
  
  def get_uphill_cruise_gear_down(self):
    return(self.ui.sp8.value())
  
  def get_downhill_gear_up(self):
    return(self.ui.sp9.value())
  
  def get_downhill_gear_down(self):
    return(self.ui.sp10.value())
  
  def get_stop_speed(self):
    return(self.ui.sp11.value())
  
  def get_uphill_border(self):
    return(self.ui.sp12.value())
  
  def get_downhill_border(self):
    return(self.ui.sp13.value())
  
  def get_gear_steps(self):
    return(self.ui.sp14.value())

  def get_stop_speed(self):
    return(self.ui.sp11.value())
  
  def get_selected_port(self):
    return(self.ui.port.currentText())
  
  def add_port(self,port):
    self.ui.port.addItem(port)
  
#  ----------Setter----------
  def set_flat_accell_gear_up(self,data):
    self.ui.sp1.setValue(data)
  
  def set_flat_accell_gear_down(self,data):
    self.ui.sp2.setValue(data)
  
  def set_flat_cruise_gear_up(self,data):
    self.ui.sp3.setValue(data)
  
  def set_flat_cruise_gear_down(self,data):
    self.ui.sp4.setValue(data)
  
  def set_uphill_accell_gear_up(self,data):
    self.ui.sp5.setValue(data)
  
  def set_uphill_accell_gear_down(self,data):
    self.ui.sp6.setValue(data)
  
  def set_uphill_cruise_gear_up(self,data):
    self.ui.sp7.setValue(data)
  
  def set_uphill_cruise_gear_down(self,data):
    self.ui.sp8.setValue(data)
  
  def set_downhill_gear_up(self,data):
    self.ui.sp9.setValue(data)
  
  def set_downhill_gear_down(self,data):
    self.ui.sp10.setValue(data)
  
  def set_stop_speed(self,data):
    self.ui.sp11.setValue(data)
  
  def set_uphill_border(self,data):
    self.ui.sp12.setValue(data)
  
  def set_downhill_border(self,data):
    self.ui.sp13.setValue(data)
  
  def set_gear_steps(self,data):
    self.ui.sp14.setValue(data)
  
  def set_send_action(self,action = lambda:print("send button pushed")):
    self.ui.send_button.clicked.connect(action)
  
  def set_reset_action(self,action = lambda:print("reset button pushed")):
    self.ui.reset_button.clicked.connect(action)
    