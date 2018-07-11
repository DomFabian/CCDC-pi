#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import RPi.GPIO as GPIO
import subprocess
import time
import atexit

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

LED_list = [LED1r, LED1g, LED2r, LED2g, LED3r, LED3g, LED4r, LED4g]

for i in LED_list:
	GPIO.setup(i, GPIO.OUT)

# Switches not yet implemented...
# SWmaster = 33
# SW1 = 29
# SW2 = 31
# SW3 = 36
# SW4 = 37
# SW = [ 0, SW1, SW2, SW3, SW4 ]
        
# switch_list = [SWmaster, SW1, SW2, SW3, SW4]
# for i in switch_list:
# 	GPIO.setup(i, GPIO.IN)

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
       for i in range(1, 4):
                mh.getMotor(i).run(Raspi_MotorHAT.RELEASE)
                GPIO.output(LEDr[i],1)
                GPIO.output(LEDg[i],0)

MOTORS = 4
MOTOR_SEGMENTS = 4
MOTOR_SPEED =    [ 0, 28, 15, 15, 28 ]
MOTOR_DURATION = [ 0, 10, 10, 10, 10.5 ]
# MOTOR_DELAY = [ 0, 5, 5, 5, 5 ]    # This took 03:55.06, so add 56:04 / 16 = 210.5.
MOTOR_DELAY = [ 0, 215.5, 215.5, 215.5, 215.5 ]

def do_motor(mot):
        motor = mh.getMotor(mot)
        print("Handling motor {}".format(mot))
        GPIO.output(LEDr[i], 0)
        GPIO.output(LEDg[i], 1)
        for segment in range(0, MOTOR_SEGMENTS):
                print("  Segment {} wait...".format(segment))
                time.sleep(MOTOR_DELAY[mot])
                print("  Segment {} motor!".format(segment))
                motor.setSpeed(MOTOR_SPEED[mot])
                motor.run(Raspi_MotorHAT.FORWARD)
                time.sleep(MOTOR_DURATION[mot])
                motor.run(Raspi_MotorHAT.RELEASE)
        print("  Done with motor {}".format(mot))
        GPIO.output(LEDr[i], 1)
        GPIO.output(LEDg[i], 0)

STATE_FILE = "/tmp/motorclock.state"

def write_state(state):
        try:
                f = open(STATE_FILE, "w")
                f.write(state + '\n')
                f.close()
                subprocess.call(["/bin/chmod", "a+w", STATE_FILE])
        except:
                pass
        
if __name__ == '__main__':
        write_state('running')
	atexit.register(turnOffMotors)
	
	#turn on all the green lights at start
        for i in range(1, MOTORS + 1):
                GPIO.output(LEDr[i], 0)
                GPIO.output(LEDg[i], 1)

        for i in range(1, MOTORS + 1):
                do_motor(i)

        write_state('expired')
