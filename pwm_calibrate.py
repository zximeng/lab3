import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)

p = GPIO.PWM(32, 46.5)  # channel=12 frequency=50Hz
p.start(7)
time.sleep(0.1)

p.stop()
GPIO.cleanup()