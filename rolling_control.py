''' 
XIMENG ZHANG (XZ737)
YIFEI XU (YX459)
LAB2
3/2/2020
'''

import pygame     # Import pygame graphics library
import os    # for OS calls
import time
import RPi.GPIO as GPIO
# GPIO init
GPIO.setmode(GPIO.BCM)
#pygame init 
pygame.init()
pygame.mouse.set_visible(False)
WHITE = 255, 255, 255
BLACK = 0,0,0
green = (0, 255, 0) 
blue = (0, 0, 128) 
screen = pygame.display.set_mode((320, 240))
my_font= pygame.font.Font(None, 50)
my_buttons= { 'quit':(160,120)}

command = ['stop', 'clockwise','counter-clockwise']

#left log queue for printing 
leftlogqueue = ['stop', 'stop','stop']
# right log queue for printing
rightlogqueue = ['stop', 'stop','stop']
# update the left queue 
leftlogqueue.pop()
leftlogqueue.append()
# update the right queue 
rightlogqueue.pop()
rightlogqueue.append()
# print the log
#initial 
toprint = logqueue[i] + timeofoperation
text = my_font.render(toprint, True, WHITE)
textRect = text.get_rect(center=(160,120))  
screen.blit(text, textRect)

pygame.display.flip()