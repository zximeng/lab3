''' 
XIMENG ZHANG (XZ737)
YIFEI XU (YX459)
LAB3
3/2/2020
'''

import pygame     # Import pygame graphics library
import os    # for OS calls
import time
import RPi.GPIO as GPIO

#pygame init 
pygame.init()
pygame.mouse.set_visible(False)
WHITE = 255, 255, 255
BLACK = 0,0,0
green = (0, 255, 0) 
blue = (0, 0, 128) 
screen = pygame.display.set_mode((320, 240))
my_font= pygame.font.Font(None, 50)
my_buttons= { 'stop':(160,120), 'quit': (160,200)}

command = ['stop', 'clockwise','counter-clockwise']

#left log queue for printing 
leftlogqueue = ['stop', 'stop','stop']
# right log queue for printing
rightlogqueue = ['stop', 'stop','stop']
#time queue for left
timeleft = ['0', '0','0']
#time queue for right
timeright = ['0', '0','0']
#left center positions
leftcenters = []
#right center positions
rightcenters = []


#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
chan_list = [17,22,23,27,19,26]

p1 = GPIO.PWM(12, 46.5)  
p2 = GPIO.PWM(16, 46.5)  
p1.start(7)
p2.start(7)
p1stop = False
p2stop = False

# def the frame-update function
def printop(number):
	# update the left queue 
	#leftlogqueue.pop()
	#leftlogqueue.append()
	# update the right queue 
	#rightlogqueue.pop()
	#rightlogqueue.append()
	if(number == 22):
		leftlogqueue.pop()
		leftlogqueue.append("stop")
	elif(number == 23):
		leftlogqueue.pop()
		leftlogqueue.append("counter-clockwise")
	elif(number == 17):
		leftlogqueue.pop()
		leftlogqueue.append("clockwise")
	elif(number == 19):
		rightlogqueue.pop()
		rightlogqueue.append("stop")
	elif(number == 26):
		rightlogqueue.pop()
		rightlogqueue.append("counter-clockwise")
	elif(number == 27):
		rightlogqueue.pop()
		rightlogqueue.append("clockwise")

	
	# print the log
	#initial
	for i in range(0,3): 
		toprint = leftlogqueue[i] + timeleft[i]
		text = my_font.render(toprint, True, WHITE)
		textRect = text.get_rect(center=(160,120))  
		screen.blit(text, textRect)

		pygame.display.flip()
	# print the center round button and quit button
	


while(True):
	GPIO.setup(chan_list,GPIO.IN,pull_up_down = GPIO.PUD_UP)
	time.sleep(0.1)
	if(not GPIO.input(22)):
		p1.stop()
		p1stop = True
	if(not GPIO.input(23)):
		if(p1stop == True):
			
			p1.start(7.83)
			p1.ChangeFrequency(46.08)
		else:			
			p1.ChangeFrequency(46.08)
			p1.ChangeDutyCycle(7.83)		
	if(not GPIO.input(17)):
		if(p1stop == True):
			
			p1.start(6.10)
			p1.ChangeFrequency(46.95)
		else:
			p1.ChangeFrequency(46.95)
			p1.ChangeDutyCycle(6.10)	
	if(not GPIO.input(19)):
		p2.stop()
		p2stop = True
	if(not GPIO.input(26)):
		if(p2stop == True):
			
			p2.start(7.83)
			p2.ChangeFrequency(46.08)
		else:
			p2.ChangeFrequency(46.08)
			p2.ChangeDutyCycle(7.83)		
	if(not GPIO.input(27)):
		if(p2stop == True):
			
			p2.start(6.10)
			p2.ChangeFrequency(46.95)
		else:
			p2.ChangeFrequency(46.95)
			p2.ChangeDutyCycle(6.10)


p1.stop()
p2.stop()
GPIO.cleanup()



