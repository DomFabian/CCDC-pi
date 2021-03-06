#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
# Motors are stupidly numbered from 1. These numbers match the
# numbers printed on the board: M1 M2 M3 M4.
myMotor = mh.getMotor(3)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor.setSpeed(150)
myMotor.run(Raspi_MotorHAT.FORWARD);
# turn on motor
myMotor.run(Raspi_MotorHAT.RELEASE);

flag = False
while (flag==False):
	for i in range(1):
		y=3
		myMotor = mh.getMotor(y)
		print 'Using Motor ' + str(y)
		myMotor.run(Raspi_MotorHAT.FORWARD)

		x=1
		while x<6:
			print x
			#print 'starting at 1'
			myMotor.setSpeed(24)
			#print 'sleeping 2'
			#time.sleep(9)
			time.sleep(9)
			#print 'slowing down to 0'
			myMotor.setSpeed(0)
			#print 'sleeping 60'
			time.sleep(1)
			#print 'resetting'
			x=x+1
		#if y == 4:
		#	flag = True
		#	print "4 motors ran, now exiting!"

'''time.sleep(10)
print "Wind them back up! "
myMotor.run(Raspi_MotorHAT.BACKWARD)

for y in range(1,5):
	myMotor = mh.getMotor(y)
	myMotor.setSpeed(22)
	time.sleep(45)
	myMotor.setSpeed(0)

print "Release"
myMotor.run(Raspi_MotorHAT.RELEASE)
time.sleep(1.0)'''

