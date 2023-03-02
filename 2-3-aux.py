import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

try:

    leds = [21, 20, 16, 12, 7, 8, 25, 24]
    aux = [22, 23, 27, 18, 15, 14, 3, 2]

    GPIO.setup(leds, GPIO.OUT)
    GPIO.setup(aux, GPIO.OUT)

    GPIO.output(aux, 1)


    while(True):
        for k in range(0,8):
            GPIO.output(leds[k], GPIO.input(aux[k]))
finally:
    GPIO.setup(aux, 0)
    GPIO.cleanup()