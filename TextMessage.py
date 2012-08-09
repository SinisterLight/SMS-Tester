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
import datetime
 
class TextMessage:

    def __init__(self, portNum,recipient="0000000", message="TextMessage.content not set."):
        self.recipient = recipient
        self.content = message
	self.portNum=str(portNum)
	self.simNumber="Random"
	self.sentMessageTimeStamp=datetime.datetime.now()

    def connectDevice(self):
        self.ser = serial.Serial('/dev/ttyUSB'+ self.portNum, 115200, timeout=5)
        time.sleep(1)

    def disconnectDevice(self):
        self.ser.close()

    def getSimNumber(self):
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,1,0,0,0\r')
	time.sleep(1)
	self.ser.write('AT+CCID\r')
	time.sleep(1)
	while  True:   
	        messages = self.ser.readline()
		if  (messages[:7] == 'AT+CCID'):
			messages=self.ser.readline()
			messages=messages[:-2]
			splitStringList=messages.split('"')
			self.simNumber=splitStringList[1]
			break

 
    def sendMessage(self):
        self.ser.write('AT+CNMI=0,1,1,1,0\r')
        time.sleep(1)
        self.ser.write('AT+CSMP=17,169,0,0\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CMGS=' + self.recipient + '\r')
	self.sentMessageTimeStamp=datetime.datetime.now()
        time.sleep(1)
        self.ser.write(self.content)
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)

    def storeSentMessage(self):
	getQuery='wget --spider http://localhost:3000/store/?'
	getQuery+='mobileNumber=' + urllib.quote(self.recipient) + '\&'
	getQuery+='smsTimeStamp=' + urllib.quote(str(self.sentMessageTimeStamp)) + '\&'
	getQuery+='smsText=' + urllib.quote(self.content) + '\&'
	getQuery+='simNumber='+urllib.quote(self.simNumber)
	print(getQuery)

 
    def readAllMessage(self):
        messages=''
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,1,0,0,0\r')
	time.sleep(1)
        self.ser.write('AT+CMGL="ALL"\r')
	time.sleep(1)
 	while  True:
	        messages = self.ser.readline()
		if  (messages[:13] == 'AT+CMGL="ALL"'):
			break	        
	while True:
		messages =self.ser.readline()
		if ( messages[:2] == 'OK' ):
			break
		print(messages[:-2])
 
    def readMessageDaemon(self):
        messages=''
	flag=0
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,2,0,0,0\r')
 	while  True:
                time.sleep(1)
	        messages = self.ser.readline()
		if  (messages[:17] == 'AT+CNMI=1,2,0,0,0'):
			flag = 1
		if ((flag == 1) & ( messages[:2] == 'OK' )):
			break	
	print ('Started Listening !')
	num = 1
	while True:
		#time.sleep(2)
		messages =self.ser.readline()
		if (len(messages) != 0):
			print(num)
			print(messages)
                        num += 1

    def storeMessageDaemon(self):
        messages=''
	csvHeader= 'simNumber;mobileNumber;smsTimeStamp;scriptTimeStamp;smsText'
	csvInit  = str( self.simNumber ) + ';'
	csv      = csvInit
	getQuery = 'wget --spider http://localhost:3000/store/?'
	getQuery+= 'simNumber=' + urllib.quote(self.simNumber) + '\&'
	store = getQuery
	flag=0
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,2,0,0,0\r')
 	while  True:
                time.sleep(1)
	        messages = self.ser.readline()
		if  (messages[:17] == 'AT+CNMI=1,2,0,0,0'):
			flag = 1
		if ((flag == 1) & ( messages[:2] == 'OK' )):
			break	
	print ('Started Listening !')
	print(csvHeader)
	textMessageStartFlag=0
	while True:
		messages =self.ser.readline()
		if (len(messages) != 0):
			if ( messages[:4] == '+CMT' ):
				textMessageStartFlag=1
				messages=messages[:-2]
				splitStringList=messages.split('"')
				store+= 'mobileNumber' + urllib.quote(splitStringList[1]) + '\&'
				csv+= splitStringList[1] + ';'
				store+= 'smsTimeStamp=' + urllib.quote(splitStringList[3]) + '\&'
				csv+= splitStringList[3] + ';'
				store+= 'scriptTimeStamp=' + urllib.quote(str(datetime.datetime.now())) + '\&'
				csv+= str(datetime.datetime.now()) + ';'
				continue
			if ( textMessageStartFlag ==1 ):
				textMessageStartFlag=0
				messages=messages[:-2]
				store+= 'smsText=' + urllib.quote(messages)
				csv+= messages
			#	print(store)
				print(csv)
				store = getQuery
				csv   = csvInit
				self.deleteAllMessage

    def deleteAllMessage(self):
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
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,1,0,0,0\r')
	time.sleep(1)
	self.ser.write('AT+CCID\r')
	time.sleep(1)
        self.ser.write('AT+CMGL="ALL"\r')
	time.sleep(1)
 	while  True: 
	        messages = self.ser.readline()
		if  (messages[:7] == 'AT+CCID'):
			messages=self.ser.readline()
			messages=messages[:-2]
			splitStringList=messages.split('"')
			simNumber=splitStringList[1]
			break	
 	while  True:
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
			getQuery+= 'mobileNumber=' + urllib.quote(splitStringList[3]) + '\&'
			getQuery+= 'smsTimeStamp=' + urllib.quote(splitStringList[5]) + '\&'
			
			continue
		if ( textMessageStartFlag ==1 ):
			textMessageStartFlag=0
			messages=messages[:-2]
			getQuery+='smsText='
			messages=urllib.quote(messages)
			getQuery+=messages
			getQuery+='\&simNumber='+urllib.quote(simNumber)
			print(getQuery)
			getQuery='wget --spider http://localhost:3000/store/?'

    def getPrepDaemon(self):
	textMessageStartFlag = 0
        messages=''
	getQuery='wget --spider http://localhost:3000/store/?'
	smsTextMessage=''
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('AT+CNMI=1,1,0,0,0\r')
	time.sleep(1)
	self.ser.write('AT+CCID\r')
	time.sleep(1)
        self.ser.write('AT+CMGL="ALL"\r')
	time.sleep(1)
 	while  True:
	        messages = self.ser.readline()
		if  (messages[:13] == 'AT+CMGL="ALL"'):
			break	        
	while True:
		time.sleep(1)
		messages =self.ser.readline()
		if ( messages[:5] == '+CMGL' ):
			textMessageStartFlag=1
			messages=messages[:-2]
			splitStringList=messages.split('"')
			getQuery+= 'mobileNumber=' + urllib.quote(splitStringList[3]) + '\&'
			getQuery+= 'smsTimeStamp=' + urllib.quote(datetime.datetime.now()) + '\&'
			
			continue
		if ( textMessageStartFlag ==1 ):
			textMessageStartFlag=0
			messages=messages[:-2]
			getQuery+='smsText='
			messages=urllib.quote(messages)
			getQuery+=messages
			getQuery+='\&simNumber='+urllib.quote(self.simNumber)
			print(getQuery)
			getQuery='wget --spider http://localhost:3000/store/?'
	
 
#Main function that calls other functions - Makes script reusable
def main():
	pass
 
if __name__ == "__main__":
	main()
