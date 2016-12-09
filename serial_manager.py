import serial
from serial.tools import list_ports
import os
import threading
import time

class SerialArduino():
  def __init__(self):
    pass

  def get_port_list(self):
    devices = []
    for info in list_ports.comports():
      devices.append(info.device)
    return(devices)

  def write_list(self,datas,port,baudrate = 9600):
    self.ser = serial.Serial(port,baudrate,timeout=0.1)
#    self.ser.baudrate = baudrate
#    self.ser.port = port
    check_thread=threading.Thread(target = lambda:self.check_and_next(datas))
    check_thread.start()
    
  def check_and_next(self,datas):
#    if(self.ser.read(1) == b'\xff'):
#      print("hoge")
    for i, data in enumerate(datas):
      print(data)
#      try:
##        self.ser.readline()#buffer clear
#        pass
#      except:
#        print("buffer clear")
#        pass
      while(1):
#        print([(bin(bytes([i]))) for i in range(255)])
        self.ser.write(bytes([data]))
#        time.sleep(0.5)
        print(i + ":wrote")
        
#      try:
        if(self.ser.read(1) == b'\xff'):#arduino answer check
          print(i + ":arduino ok")
          break
#        elif(self.ser.read(1) == b'\x00'):
#          print("retry")
#          pass
        else:
#          time.sleep(0.5)
          print(i + ":retry")
          pass
#      except:
#        time.sleep(0.5)
#        print("except")
#        pass
    print("Completed writing of config data.")
    self.ser.close()
    
#  def test(self):
#    self.ser = serial.Serial(port,baudrate)