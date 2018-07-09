#!/usr/bin/python
import atexit
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED1r = 8
LED1g = 10
LED2r = 11
LED2g = 12
LED3r = 13
LED3g = 7
LED4r = 21
LED4g = 23
LEDg = [ 0, LED1g, LED2g, LED3g, LED4g ]
LEDr = [ 0, LED1r, LED2r, LED3r, LED4r ]

SWmaster = 33
SW1 = 29
SW2 = 31
SW3 = 36
SW4 = 37
SW = [ 0, SW1, SW2, SW3, SW4 ]
        
LED_list = [LED1r, LED1g, LED2r, LED2g, LED3r, LED3g, LED4r, LED4g]
switch_list = [SWmaster, SW1, SW2, SW3, SW4]
for i in LED_list:
	GPIO.setup(i, GPIO.OUT)
for i in switch_list:
	GPIO.setup(i, GPIO.IN)

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
        GPIO.output(LED1r, 0)
	GPIO.output(LED2r, 0)
	GPIO.output(LED3r, 0)
	GPIO.output(LED4r, 0)
        GPIO.output(LED1g, 0)
	GPIO.output(LED2g, 0)
	GPIO.output(LED3g, 0)
	GPIO.output(LED4g, 0)

if __name__ == '__main__':
        turnOffMotors()
	atexit.register(turnOffMotors)

        if len(sys.argv) < 3:
                print("Usage: motorup.py <motor-number-1-4> <b(ackward)|f(orward)>")
                exit(1)

        mot = int(sys.argv[1])
        print("Upping motor {}.".format(mot))

        if mot < 1 or 4 < mot:
                print("Invalid motor number.")
                exit(1)

        dir_letter = sys.argv[2]
        if dir_letter != 'f' and dir_letter != 'b':
                print("Invalid direction '{}'; must be 'b' or 'f'.".format(dir_letter))
                exit(1)

        direction = Raspi_MotorHAT.BACKWARD
        if dir_letter == 'f':
                direction = Raspi_MotorHAT.FORWARD

        sys.stdout.write("Hit Ctrl-C to stop....")
        sys.stdout.flush()

	#turn on all the green lights at start
        GPIO.output(LEDr[mot],1)
        GPIO.output(LEDg[mot],1)
        motor = mh.getMotor(mot)
        motor.setSpeed(50)
        motor.run(direction)

        while True:
                time.sleep(1)
        exit(0)
