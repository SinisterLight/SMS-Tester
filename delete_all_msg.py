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


usb_serial = ATcommands() 
usb_serial.connectDevice()
sms = TextMessage()
sms.deleteAllMessage()
usb_serial.disconnectDevice()
 
#Main function that calls other functions - Makes script reusable
def main():
	pass
 
if __name__ == "__main__":
	main()