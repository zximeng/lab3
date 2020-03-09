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
from pygame.locals import *   # for event MOUSE variables

#pygame init 
pygame.init()
pygame.mouse.set_visible(True)
WHITE = 255, 255, 255
BLACK = 0,0,0
RED=255,0,0

green = (0, 255, 0) 
blue = (0, 0, 128) 
screen = pygame.display.set_mode((320, 240))
my_font= pygame.font.Font(None, 24)
my_buttons= { 'STOP':(140,120), 'QUIT':(300,220)}
my_buttons2= { 'Resume':(140,120), 'QUIT':(300,220)}

command = ['stop', 'clockwise','counter-clockwise']

history = ['left history', 'right history']
#left log queue for printing 
leftlogqueue = ['stop', 'stop','stop']
# right log queue for printing
rightlogqueue = ['stop', 'stop','stop']
#time queue for left
timeleft = ['0', '0','0']
#time queue for right
timeright = ['0', '0','0']
#left center positions
leftcenters = [(30,60),(30,120),(30,180)]
#right center positions
rightcenters = [(240,60),(240,120),(240,180)]
#history center
hc = [(50,10),(220,10)]


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
firsttime = time.time()

# flag to track whether emergency stop has been clicked. 
estop = False
# def the frame-update function
def printop(number):
	# update the left queue 
	#leftlogqueue.pop()
	#leftlogqueue.append()
	# update the right queue 
	#rightlogqueue.pop()
	#rightlogqueue.append()
	screen.fill(BLACK)
	if(number == 22):
		leftlogqueue.pop(0)
		leftlogqueue.append("stop")
		timeleft.pop(0)
		timepast = time.time() - firsttime
		timeleft.append(str(int(timepast)))
	elif(number == 23):
		leftlogqueue.pop(0)
		leftlogqueue.append("counter-clockwise")
		timeleft.pop(0)
		timepast = time.time() - firsttime
		timeleft.append(str(int(timepast)))
	elif(number == 17):
		leftlogqueue.pop(0)
		leftlogqueue.append("clockwise")
		timeleft.pop(0)
		timepast = time.time() - firsttime
		timeleft.append(str(int(timepast)))
	elif(number == 19):
		rightlogqueue.pop(0)
		rightlogqueue.append("stop")
		timeright.pop(0)
		timepast = time.time() - firsttime
		timeright.append(str(int(timepast)))
	elif(number == 26):
		rightlogqueue.pop(0)
		rightlogqueue.append("counter-clockwise")
		timeright.pop(0)
		timepast = time.time() - firsttime
		timeright.append(str(int(timepast)))
	elif(number == 27):
		rightlogqueue.pop(0)
		rightlogqueue.append("clockwise")
		timeright.pop(0)
		timepast = time.time() - firsttime
		timeright.append(str(int(timepast)))

	
	# print the log
	#initial
	for i in range(0,2):
		toprint = history[i]
		text = my_font.render(toprint, True, WHITE)
		textRect = text.get_rect(center=hc[i]) 
		# print logqueue[i] + timequeue[i] at centerqueue[i]
		screen.blit(text, textRect)
	for i in range(0,3): 
		toprint = leftlogqueue[i] + timeleft[i]
		text = my_font.render(toprint, True, WHITE)
		textRect = text.get_rect(center=leftcenters[i]) 
		# print logqueue[i] + timequeue[i] at centerqueue[i]
		screen.blit(text, textRect)
	for i in range(0,3): 
		toprint = rightlogqueue[i] + timeright[i]
		text = my_font.render(toprint, True, WHITE)
		textRect = text.get_rect(center=rightcenters[i]) 
		# print logqueue[i] + timequeue[i] at centerqueue[i]
		screen.blit(text, textRect)
	if(not estop):
		pygame.draw.circle(screen, RED, [140, 120], 30)
		for (my_text, text_pos) in my_buttons.items():    
			text_surface = my_font.render(my_text, True, WHITE)    
			rect = text_surface.get_rect(center=text_pos)
			#print(my_text)
			#print(my_buttons)
			screen.blit(text_surface, rect)
	else:
		pygame.draw.circle(screen, green, [140, 120], 30)
		for (my_text, text_pos) in my_buttons2.items():    
			text_surface = my_font.render(my_text, True, WHITE)    
			rect = text_surface.get_rect(center=text_pos)
			#print(my_text)
			#print(my_buttons)
			screen.blit(text_surface, rect)
	
	

	pygame.display.flip()
	# print the center round button and quit button
	

flag = True
stopall = False
while(flag):
	GPIO.setup(chan_list,GPIO.IN,pull_up_down = GPIO.PUD_UP)
	#screen.fill(BLACK)

	#if y<144&y>96:
	#	if x<  x>:
	#		flag = False
			
	#if  :
	#	if  :
	#		printop(19)
	#		printop(22)
	
			
	    
	time.sleep(0.1)
	printop(0)
	if(not stopall):
		if(not GPIO.input(22)):
			p1.stop()
			p1stop = True
			printop(22)
		if(not GPIO.input(23)):
			printop(23)
			if(p1stop == True):
				
				p1.start(7.83)
				p1.ChangeFrequency(46.08)
			else:			
				p1.ChangeFrequency(46.08)
				p1.ChangeDutyCycle(7.83)		
		if(not GPIO.input(17)):
			printop(17)
			if(p1stop == True):
				
				p1.start(6.10)
				p1.ChangeFrequency(46.95)
			else:
				p1.ChangeFrequency(46.95)
				p1.ChangeDutyCycle(6.10)	
		if(not GPIO.input(19)):
			printop(19)
			p2.stop()
			p2stop = True
		if(not GPIO.input(26)):
			printop(26)
			if(p2stop == True):
				
				p2.start(7.83)
				p2.ChangeFrequency(46.08)
			else:
				p2.ChangeFrequency(46.08)
				p2.ChangeDutyCycle(7.83)		
		if(not GPIO.input(27)):
			printop(27)
			if(p2stop == True):
				
				p2.start(6.10)
				p2.ChangeFrequency(46.95)
			else:
				p2.ChangeFrequency(46.95)
				p2.ChangeDutyCycle(6.10)
	for event in pygame.event.get():
		if(event.type is MOUSEBUTTONUP):
			pos = pygame.mouse.get_pos() 
			x,y = pos
			if(x<180 and x> 100):
				if(y<140 and y > 100):
					if (estop == False):
						estop = not estop
						p1.stop()
						p2.stop()
						p1stop = True
						p2stop = True
						stopall = True	
					else:
						stopall = False
					printop(0)
			if(x>200):
				if(y>200):
					flag = False

p1.stop()
p2.stop()
GPIO.cleanup()



