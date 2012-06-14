#!/usr/bin/env python
"""
#Use this to call the sms function
#It is for sending SMS using AT commands - version v3
"""
## The packges below must be installed in advance
## install python-setuptools
## install pyserial
 
import serial
import time
import sys
 
from at_cmds import ATcommands
from txt_msg import TextMessage

portHash= { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15' }

for i in range( len(portHash) )
	usb_serial = ATcommands() 
	usb_serial.connectDevice(portHash[i])
	sms = TextMessage(portHash[i])
	sms.getPrep()
	sms.deleteAllMessages()
	usb_serial.disconnectDevice()
 

#Main function that calls other functions - Makes script reusable
def main():
	pass
 
if __name__ == "__main__":
	main()
