import serial
import time
ser=serial.Serial("/dev/ttyS0",baudrate=9600)
while True:
	ser.write("Hello")
