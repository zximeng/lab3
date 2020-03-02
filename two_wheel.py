import time
import RPi.GPIO as GPIO
import numpy as np
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
chan_list = [17,22,23,27,19,26]

p1 = GPIO.PWM(12, 46.5)  
p2 = GPIO.PWM(16, 46.5)  
p1.start(7)
p2.start(7)
while(True):
	GPIO.setup(chan_list,GPIO.IN,pull_up_down = GPIO.PUD_UP)
	time.sleep(0.1)
	if(not GPIO.input(22)):
		p1.ChangeFrequency(46.5)
		p1.ChangeDutyCycle(7)
	if(not GPIO.input(23)):
		p1.ChangeFrequency(46.08)
		p1.ChangeDutyCycle(7.83)		
	if(not GPIO.input(17)):
		p1.ChangeFrequency(46.95)
		p1.ChangeDutyCycle(6.10)	
	if(not GPIO.input(19)):
		p2.ChangeFrequency(46.5)
		p2.ChangeDutyCycle(7)
	if(not GPIO.input(26)):
		p2.ChangeFrequency(46.08)
		p2.ChangeDutyCycle(7.83)		
	if(not GPIO.input(27)):
		p2.ChangeFrequency(46.95)
		p2.ChangeDutyCycle(6.10)


p1.stop()
p2.stop()
GPIO.cleanup()
