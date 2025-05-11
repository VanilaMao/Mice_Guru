import serial
from serial.tools import list_ports
import time
from enum import Enum

#'0' touch left, '1' touch right, '2':record stop, stop food spendor, '3' start food spendor
class ArduinoCommand(str,Enum):
     Left = '0'
     Right = '1'
     Stop ='2'
     Start ='3'

class Arduino:
    _instance = None
    def __init__(self,port, baudrate=115200, timeout=.1):
        if self._instance is None:
            self._device = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
            self._instance = self

    @staticmethod
    def instance():
        if Arduino._instance is None:
            port = Arduino.find_arduino_port()
            if port is not None:
                Arduino._instance = Arduino(port)
            else:
                print("Arduino serial port is not available")           
        return Arduino._instance
    
    @staticmethod
    def find_arduino_port():
        ports = list(list_ports.comports())
        for port in ports:
            if "Arduino" in port.manufacturer or "CH340" in port.description:
                return port.device
        return None

    def write(self,command:ArduinoCommand):
        self._device.write(bytes(command.value,  'utf-8'))

    def read(self):
        return self._device.read()
    
    def close(self):
        self._device.close()

if __name__ == "__main__":
    ar = Arduino.instance()
    # a = input()
    ar.write(ArduinoCommand.Right)
    time.sleep(0.05)
    data = ar.read()
    print(data)
    ar.close()