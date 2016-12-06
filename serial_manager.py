import serial
from serial.tools import list_ports
import os
import threading

class SerialArduino():
  def __init__(self):
    self.ser = serial.Serial()
    self.ser.baudrate = 9600
    self.devices = self.get_port_list()
    self.selected_port = None

  def get_port_list(self):
    devices = []
    for info in list_ports.comports():
      devices.append(info.device)
    return(devices)

  def write_list(self,datas,port):
    self.ser.port = port
    check_thread=threading.Thread(target = lambda:self.check_and_next(datas))
    check_thread.start()
    
  def check_and_next(self,datas):
    for data in datas:
      self.ser.readline()#buffer clear
      
      while(1):
        ser.write(data.to_bytes(1,'big'))
        time.sleep(0.05)
        if(ser.read(1) == 255):#arduino answer check
          break
        else:
          pass
