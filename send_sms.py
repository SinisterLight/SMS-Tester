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
 
if len(sys.argv) > 1:
	phoneNumber = sys.argv[1]
	message = ""	
	if len(sys.argv) >= 2:
		for i in range(2, len(sys.argv)):
			message = message + " " + sys.argv[i] 
 
		message = message.strip()
	print "number = " + phoneNumber + ", message = " + message
	sms = TextMessage('0',phoneNumber, message)
else:
	sms = TextMessage('0')	
 
usb_serial = ATcommands()
 
usb_serial.connectDevice('0')
sms.sendMessage()
usb_serial.disconnectDevice()
 
#Main function that calls other functions - Makes script reusable
def main():
	pass
 
if __name__ == "__main__":
	main()
