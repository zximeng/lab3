import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)

p = GPIO.PWM(32, 46.5)  # channel=12 frequency=50Hz
p.start(7)
time.sleep(3)
# 1.7 - 1.5 / 10 = 0.02ms 
# each step would be 0.02 ms
# to rotate clockwise, from 1.5 to 1.3 
# to rotate counter-clockwise, from 
for x in range(0, 10):
    newduty = 1.5 

p.stop()
GPIO.cleanup()