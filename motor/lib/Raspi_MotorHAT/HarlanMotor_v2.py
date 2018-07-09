#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import RPi.GPIO as GPIO
import time
import atexit

GPIO.setmode(GPIO.BOARD)
LED1r = 8
LED1g = 10
LED2r = 11
LED2g = 12
LED3r = 13
LED3g = 15
LED4r = 21
LED4g = 23

SWmaster = 25
SW1 = 29
SW2 = 31
SW3 = 36
SW4 = 37

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



if __name__ == '__main__':
	atexit.register(turnOffMotors)
	
	#turn on all the green lights at start
	GPIO.output(LED1g,1)
	GPIO.output(LED2g,1)
	GPIO.output(LED3g,1)
	GPIO.output(LED4g,1)

	################################# DC motor test!
	# Motors are stupidly numbered from 1. These numbers match the
	# numbers printed on the board: M1 M2 M3 M4.
	#myMotor = mh.getMotor(3)

	# set the speed to start, from 0 (off) to 255 (max speed)
	#myMotor.setSpeed(150)
	#myMotor.run(Raspi_MotorHAT.FORWARD);
	# turn on motor
	#myMotor.run(Raspi_MotorHAT.RELEASE);
	while True:
		flag = False
		if (SWmaster == 1):
			while (flag==False):
				for y in range(1,5):
					if y == 2:
						GPIO.output(LED1g,0)
						GPIO.output(LED1r,1)
					if y == 3:
						GPIO.output(LED2g,0)
						GPIO.output(LED2r,1)
					if y == 4:
						GPIO.output(LED3g,0)
						GPIO.output(LED3r,1)
					myMotor = mh.getMotor(y)
					print 'Using Motor ' + str(y)
					myMotor.run(Raspi_MotorHAT.FORWARD)

					x=1
					while x<6:
						#print x
						#play with these variables for length of drop...5 drops somewhere between 20-25 speed and 8-9.5sec seemed right
						myMotor.setSpeed(24)
						time.sleep(9)
						myMotor.setSpeed(0)
						#add the 3 minute wait here
						time.sleep(171)
						x=x+1
					myMotor.run(Raspi_MotorHAT.RELEASE)
					time.sleep(1.0)
					if y == 4:
						GPIO.output(LED4g,0)
						GPIO.output(LED4r,1)
						flag = True
						print "4 motors ran, now exiting!"
		elif ((GPIO.input(SW1)==1) and (GPIO.input(SWmaster) ==0)):
			myMotor = mh.getMotor(1)
			myMotor.run(Raspi_MotorHAT.BACKWARD)
			while GPIO.input(SW1) == 1:
				myMotor.setSpeed(40)
		elif ((GPIO.input(SW2)==1) and (GPIO.input(SWmaster) ==0)):
			myMotor = mh.getMotor(2)
			myMotor.run(Raspi_MotorHAT.BACKWARD)
			while GPIO.input(SW2) == 1:
				myMotor.setSpeed(40)
		elif ((GPIO.input(SW3)==1) and (GPIO.input(SWmaster) ==0)):
			myMotor = mh.getMotor(3)
			myMotor.run(Raspi_MotorHAT.BACKWARD)
			while GPIO.input(SW3) == 1:
				myMotor.setSpeed(40)
		elif ((GPIO.input(SW4)==1) and (GPIO.input(SWmaster) ==0)):
			myMotor = mh.getMotor(4)
			myMotor.run(Raspi_MotorHAT.BACKWARD)
			while GPIO.input(SW4) == 1:
				myMotor.setSpeed(40)
		

	'''time.sleep(10)
	print "Wind them back up! "
	myMotor.run(Raspi_MotorHAT.BACKWARD)
	
	print "Release"
	myMotor.run(Raspi_MotorHAT.RELEASE)
	time.sleep(1.0)'''
