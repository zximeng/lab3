import time
import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)

p = GPIO.PWM(32, 46.5)  
p.start(7)
time.sleep(3)
# 1.7 - 1.5 / 10 = 0.02ms 
# each step would be 0.02 ms
# to rotate clockwise, from 1.5 to 1.3 
# to rotate counter-clockwise, from 
newduty = 1.5
for x in range(0, 10):
    newduty = newduty  - 0.02
    newfreq = 1000 / ( newduty + 20)
    newdc = (newduty / (newduty+20)) * 100
    p.ChangeFrequency(newfreq)
    p.ChangeDutyCycle(newdc)
    print('clockwise phase: ' + str(x))
    print("current frequence: "+ str(newfreq) +"pulse width:"+ str(newduty) + "duty cycle: "+ str(newdc))
    if x == 4:
        print('halfway there')
        os.system('scrot')
    elif x == 9:
        print('full speed')
        os.system('scrot')
    time.sleep(3)
newduty = 1.5
for x in range(0, 10):
    newduty = newduty + 0.02
    newfreq = 1000 / ( newduty + 20)
    newdc = (newduty / (newduty+20)) * 100
    p.ChangeFrequency(newfreq)
    p.ChangeDutyCycle(newdc) 
    print('counter-clockwise phase: ' + str(x))
    print("current frequence: "+ str(newfreq) +"pulse width:"+ str(newduty) + "duty cycle: "+ str(newdc))
    if x == 4:
        print('halfway there')
        os.system('scrot')
    elif x == 9:
        print('full speed')
        os.system('scrot')
    time.sleep(3)
print('back to idle')
os.system('scrot')
p.ChangeFrequency(46.5) # back to idle
p.ChangeDutyCycle(7) 


p.stop()
GPIO.cleanup()
