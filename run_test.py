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
os.putenv('SDL_VIDEODRIVER', 'fbcon')   # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')     
os.putenv('SDL_MOUSEDRV', 'TSLIB')     # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
#pygame init 
pygame.init()
pygame.mouse.set_visible(False)
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
step = 0
flag = True
stopall = False
estop = False
starttime = time.time()
leftstate = "stop"
rightstate = "stop"
GPIO.setup(chan_list,GPIO.IN,pull_up_down = GPIO.PUD_UP)
currentstep = 0

def stopmotor():
	global estop
	currenttime = time.time()
	timepast = 0
	#stop
	while(timepast < 3 and not estop):
		p1.stop()
		printop(22)
		p2.stop()
		printop(19)
		timepast = time.time() - currenttime
		checkforstop()
def movebackward():
	global estop
	currenttime = time.time()
	timepast = 0
	# Move the robot forward about 1 foot 
	while(timepast < 3 and not estop):
		p1.start(6.54)
		p1.ChangeFrequency(46.73)
		printop(17)
		p2.start(7.4)
		p2.ChangeFrequency(46.3)
		printop(26)
		timepast = time.time() - currenttime
		checkforstop()
def pivotleft():
	global estop
	currenttime = time.time()
	timepast = 0
	#pivot left
	while(timepast < 3 and not estop):
		p1.start(7.4)
		p1.ChangeFrequency(46.3)
		printop(17)
		p2.stop()
		printop(19)
		timepast = time.time() - currenttime
		checkforstop()
def pivotright():
	global estop
	currenttime = time.time()
	timepast = 0
	#pivot right
	while(timepast < 3 and not estop):
		p2.start(6.54)
		p2.ChangeFrequency(46.73)
		printop(26)
		p1.stop()
		printop(22)
		timepast = time.time() - currenttime
		checkforstop()
def moveforward1():
	global estop
	currenttime = time.time()
	timepast = 0
	#backward 1 foot
	while(timepast < 3 and not estop):
		p2.start(6.54)
		p2.ChangeFrequency(46.73)
		printop(27)
	
		p1.start(7.4)
		p1.ChangeFrequency(46.3)

		printop(23)
		timepast = time.time() - currenttime
		checkforstop()
		
		


# flag to track whether emergency stop has been clicked. 

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
	
# run at half speed 1.4 ms & 1.6ms 
# motors should rotate in different directions to move forward
# 
# Run a while loop for each action with timer waiting for the same time. 
# Record start before the while loop and end while if time is up.  

def checkforstop():  
	global estop
	global stopall
	global step
	global currentstep
	global flag
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
						currentstep = step
						step = 7
					else:
						stopall = False
						estop = not estop
						step = currentstep						
			if(x>200):
				if(y>200):
					flag = False 


# main function: 
while(flag): 
	time.sleep(0.1)
	printop(0) 

	checkforstop()
	# Move the robot forward about 1 foot 
	if step == 0 and not estop :
		moveforward1()
		step+=1
	#stop
	checkforstop()
	if flag == False: break
	if step ==1 and not estop: 
		stopmotor()
		step+=1
	#backward 1 foot
	checkforstop()
	if flag == False: break
	if step ==2 and not estop: 
		movebackward()
		step+=1
	checkforstop()
	if flag == False: break
	#pivot left 
	if step ==3 and not estop: 
		pivotleft()
		step+=1
	#stop
	checkforstop()
	if flag == False: break
	if step ==4 and not estop: 
		stopmotor()
		step+=1
	#pivot right
	checkforstop()
	if step ==5 and not estop: 
		pivotright()
		step+=1
	#stop()
	checkforstop()
	if flag == False: break
	if step ==6 and not estop: 
		stopmotor()
	step = 0
	checkforstop()



p1.stop()
p2.stop()
GPIO.cleanup()



