import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
t=GPIO.PWM(3,80)
GPIO.output(3,True)
while True:
	t.start(30)