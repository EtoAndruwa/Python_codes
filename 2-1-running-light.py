import RPi.GPIO as GPIO
import time
leds = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for i in range(0,3):
    for k in range(0, 8):
        GPIO.output(leds[k], 1)
        time.sleep(0.2)
        GPIO.output(leds[k], 0)

GPIO.output(leds, 0)
GPIO.cleanup()
