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

from TextMessage import TextMessage
 
if len(sys.argv) > 1:
	portNumber = sys.argv[1]
	phoneNumber = sys.argv[2]
	message = ""	
	if len(sys.argv) >= 3:
		for i in range(3, len(sys.argv)):
			message = message + " " + sys.argv[i] 
 
		message = message.strip()
	print "echo "+"'number = " + phoneNumber + ", message = " + message + "'"
	sms = TextMessage(portNumber,phoneNumber, message)
else:
	sms = TextMessage('0')	

 
sms.connectDevice()
sms.getSimNumber()
sms.sendMessage()
sms.storeSentMessage()
sms.disconnectDevice()
 
#Main function that calls other functions - Makes script reusable
def main():
	pass
 
if __name__ == "__main__":
	main()
