import os
import serial
import RPi.GPIO as GPIO
import time
ser=serial.Serial("/dev/ttyS0",baudrate=9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,True)
char=''
string=''
while True:
	while char!='#':
		char=ser.read()
		string=string+char
	if(string.find("LED on"):
		GPIO.output(3,False)
	if(string.find("LED off"):
		GPIO.output(3,True)
	ser.flush()
	char=''
	string='' 