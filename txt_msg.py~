#!/usr/bin/env python
"""
txt_msg.py - All AT commands and all classes are here. Call them from outside. 
"""
## The packges below must be installed in advance
## install python
## install pyserial
 
import serial
import time
import re
import urllib

 
class TextMessage:
    def __init__(self, portNum,recipient="0000000", message="TextMessage.content not set."):
        self.recipient = recipient
        self.content = message
	self.portNum=portNum
 
    def sendMessage(self):
        self.ser = serial.Serial('/dev/ttyUSB'+self.portNum, 115200, timeout=5)
        self.ser.write('AT+CNMI=0,1,1,1,0\r')
        time.sleep(1)
        self.ser.write('AT+CSMP=17,169,0,0\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
       # self.ser.write('AT+CSCA=""')
       # time.sleep(1)
        self.ser.write('AT+CMGS=' + self.recipient + '\r')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)
 
    def readAllMessage(self):
        messages=''
        self.ser = serial.Serial('/dev/ttyUSB'+self.portNum, 115200, timeout=5)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,1,0,0,0\r')
	time.sleep(1)
        self.ser.write('AT+CMGL="ALL"\r')
	time.sleep(1)
 	while  True:  #(messages != NULL):
               # time.sleep(1)
	        messages = self.ser.readline()
		if  (messages[:13] == 'AT+CMGL="ALL"'):
			break	        
	while True:
		#time.sleep(1)
		messages =self.ser.readline()
		if ( messages[:2] == 'OK' ):
			break
		#print len(messages)
		print(messages[:-2])
 
    def readMessageDaemon(self):
        messages=''
	flag=0
        self.ser = serial.Serial('/dev/ttyUSB'+self.portNum, 115200, timeout=5)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,2,0,0,0\r')
 	while  True:  #(messages != NULL):
                time.sleep(1)
	        messages = self.ser.readline()
		if  (messages[:17] == 'AT+CNMI=1,2,0,0,0'):
			flag = 1
		if ((flag == 1) & ( messages[:2] == 'OK' )):
			break	
	print ('Started Listening !')
	while True:
	
		time.sleep(2)
		messages =self.ser.readline()
		print(messages)

    def deleteAllMessage(self):
        self.ser = serial.Serial('/dev/ttyUSB'+self.portNum, 115200, timeout=5)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CMGD=1,4\r')
	time.sleep(1)

    def getPrep(self):
	textMessageStartFlag = 0
        messages=''
	getQuery='wget --spider http://localhost:3000/store/?'
	simNumber=''
	smsTextMessage=''
        self.ser = serial.Serial('/dev/ttyUSB'+self.portNum, 115200, timeout=5)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,1,0,0,0\r')
	time.sleep(1)
	self.ser.write('AT+CCID\r')
	time.sleep(1)
        self.ser.write('AT+CMGL="ALL"\r')
	time.sleep(1)
 	while  True:  #(messages != NULL): 
	        messages = self.ser.readline()
		if  (messages[:7] == 'AT+CCID'):
			messages=self.ser.readline()
			messages=messages[:-2]
			splitStringList=messages.split('"')
			simNumber=splitStringList[1]
			break	
 	while  True:  #(messages != NULL): 
	        messages = self.ser.readline()
		if  (messages[:13] == 'AT+CMGL="ALL"'):
			break	        
	while True:
		messages =self.ser.readline()
		if ( messages[:2] == 'OK' ):
			break
		if ( messages[:5] == '+CMGL' ):
			textMessageStartFlag=1
			messages=messages[:-2]
			splitStringList=messages.split('"')
			#for i in range( len(splitStringList) ):
			#	print ( splitStringList[i] )
			#print (splitStringList[3])
			#print (splitStringList[5])
			getQuery+= 'mobileNumber=' + urllib.quote(splitStringList[3]) + '\&'
			##messages=splitStringList[5]
			##splitStringList=messages.split(',')
			getQuery+= 'smsTimeStamp=' + urllib.quote(splitStringList[5]) + '\&'
			
			continue
		if ( textMessageStartFlag ==1 ):
			textMessageStartFlag=0
			messages=messages[:-2]
			getQuery+='smsText='
		#	splitStringList=messages.split(' ')
		#	for i in range( len(splitStringList)-1 ):
		#		getQuery+=splitStringList[i]+'+'
		#	getQuery+=splitStringList[len(splitStringList)-1]
			messages=urllib.quote(messages)
			getQuery+=messages
			getQuery+='\&simNumber='+urllib.quote(simNumber)
			print(getQuery)
			getQuery='wget --spider http://localhost:3000/store/?'
		#print len(messages)
		#print(messages[:-2])
	
 
#Main function that calls other functions - Makes script reusable
def main():
	pass
 
if __name__ == "__main__":
	main()
