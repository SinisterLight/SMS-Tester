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

if len(sys.argv) > 2:
	for i in range( 0,int(sys.argv[2]) ):
		sms = TextMessage(i)
		sms.getSimNumber()
		sms.connectDevice()
		sms.getPrep()
		sms.deleteAllMessage()
else:
	sms = TextMessage(int(sys.argv[1]))
	sms.getSimNumber()
	sms.connectDevice()
	sms.getPrepDaemon()
	sms.deleteAllMessage()


#Main function that calls other functions - Makes script reusable
def main():
	pass
 
if __name__ == "__main__":
	main()
