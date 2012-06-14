#!/usr/bin/env python
"""
at_cmds.py - All AT commands and all classes are here. Call them from outside. 
"""
## The packges below must be installed in advance
## install python
## install pyserial
 
import serial
import time
 
class ATcommands:
    def setDialledNumber(self, number):
        self.dialledNumber = number
 
    def setRecipient(self, number):
        self.recipient = number
 
    def setContent(self, message):
        self.content = message
 
    def connectDevice(self,portNum):
        self.ser = serial.Serial('/dev/ttyUSB'+ portNum, 115200, timeout=5)
        time.sleep(1)
	self.ser.write('AT\r')
	time.sleep(1)
	atReply=self.ser.readline()
 
    def disconnectDevice(self):
        self.ser.close()
 
 
 
#Main function that calls other functions - Makes script reusable
def main():
	pass
 
if __name__ == "__main__":
	main()
