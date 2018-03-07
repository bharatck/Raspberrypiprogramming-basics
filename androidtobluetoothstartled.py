import RPi.GPIO as GPIO
import time
import serial
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3,True)
ser=serial.Serial("/dev/ttyS0",baudrate=9600)
while True:
	x=ser.read()
	if(x=='U'):
		GPIO.output(3,False)
	if(x=='D'):
		GPIO.output(3,True)