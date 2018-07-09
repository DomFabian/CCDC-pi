#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED1r = 8
LED1g = 10
LED2r = 11
LED2g = 12
LED3r = 13
LED3g = 7
LED4r = 21
LED4g = 23

SWmaster = 25
SW1 = 29
SW2 = 31
SW3 = 36
SW4 = 37

LED_list = [LED1r, LED1g, LED2r, LED2g, LED3r, LED3g, LED4r, LED4g]
switch_list = [SWmaster, SW1, SW2, SW3, SW4]

GPIO.setup(LED1r, GPIO.OUT)
GPIO.setup(LED1g, GPIO.OUT)
GPIO.setup(LED2r, GPIO.OUT)
GPIO.setup(LED2g, GPIO.OUT)
GPIO.setup(LED3g, GPIO.OUT)
GPIO.setup(LED3r, GPIO.OUT)
GPIO.setup(LED4g, GPIO.OUT)
GPIO.setup(LED4r, GPIO.OUT)


GPIO.output(LED1g,1)
GPIO.output(LED2g,1)
GPIO.output(LED3g,1)
GPIO.output(LED4g,1)
GPIO.output(LED1r,1)
GPIO.output(LED2r,1)
GPIO.output(LED3r,1)
GPIO.output(LED4r,1)


print 'sleeping'
time.sleep(10)

GPIO.output(LED2g,0)
GPIO.output(LED1r,1)
GPIO.output(LED2r,1)
GPIO.output(LED3r,1)
GPIO.output(LED4r,1)
GPIO.output(LED2g,0)
GPIO.output(LED3g,0)
GPIO.output(LED4g,0)



GPIO.cleanup()
