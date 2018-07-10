#!/usr/bin/python3

import time
import RPi.GPIO as io
from os import remove

guess = '0'
correct_guess = '377'

io.setmode(io.BOARD)
io.setwarnings(False)

# define the pins
led_green = 16
led_red = 12
bit = [40,38,36,32,26,24,22,18]

io.setup(led_red, io.OUT)
io.setup(led_green, io.OUT)

for b in bit:
    io.setup(b, io.OUT)


def write_binary(num):
    ''' This function takes a string argument num
        and writes each of the bits to the LED pins.
        The string must be length 8 for the 8 LEDs
        connected to the GPIO pins. The leftmost bit
        in the string (index 0) is the MSB, so it goes
        to index 0 of the bit list, etc. '''

    num = str(num)
    if len(num) != 8:
        return False

    for i in range(0,8):
        if num[i] == '1':
            io.output(bit[i], io.HIGH)
        else:
            io.output(bit[i], io.LOW)

    return True


def blink_good():
    ''' This function does a quick series of blinks of all
        of the LEDs that display the binary numbers. '''

    blink_time = .2
    num_blinks = 3
    for i in range(0,num_blinks):
        write_binary('11111111')
        time.sleep(blink_time)
        write_binary('00000000')
        time.sleep(blink_time)
    write_binary('11111111')

def blink_bad():
    ''' This function does a quick series of blinks of all
        of the LEDs that display the binary numbers. '''

    blink_time = 0.02
    num_blinks = 50
    for i in range(0,num_blinks):
        write_binary('11111111')
        time.sleep(blink_time)
        write_binary('00000000')
        time.sleep(blink_time)

def new_solution_available():
    ''' When sending the solution guesses to this Pi,
        another host will send a file over a network
        to this Pi via SCP. This function checks to see
        if that file exists. If it does exist, the contents
        of the file are placed in global variable 'guess'
        then delete the file.
        Return True if a new solution file was present,
        False otherwise. '''

    global guess
    filename = '/home/pi/CCDC-pi/binary/binary_soln'
    try:
        f = open(filename, 'r')
        guess = f.readline().strip()
        f.close()
        remove(filename)
        return True
    except:
        pass
    return False

def indicate_success():
    ''' Set the red/green LEDs to the success state. '''
    io.output(led_green, io.HIGH)
    io.output(led_red, io.LOW)

def indicate_failure():
    ''' Set the red/green LEDs to the failure state. '''
    io.output(led_green, io.LOW)
    io.output(led_red, io.HIGH)

STATE_FILE = "/home/pi/CCDC-pi/binary/state.txt"

def write_state(state):
    ''' Write the value of 'state' on a line to the puzzle's state file. '''

    try:
        f = open(STATE_FILE, 'w')
        f.write(str(state) + '\n')
        f.close()
    except:
        pass

fibonacci = ['00000000', '00000001', '00000001', '00000010', '00000011', '00000101', '00001000',
             '00001101', '00010101', '00100010', '00110111', '01011001', '10010000', '11101001']

write_binary('00000000')
indicate_failure()
write_state('running')

index = 0
while True:
    if new_solution_available():
        if guess == correct_guess:
            indicate_success()
            blink_good()
            write_state('solved')
        else:
            write_state('running-{}'.format(guess))
            indicate_failure()
            blink_bad()

    if guess != correct_guess:
        write_binary(fibonacci[index])
        index = (index + 1) % len(fibonacci)
        time.sleep(2)
        write_binary('00000000')

    time.sleep(1)

io.output(led_green, io.HIGH)
io.output(led_red, io.LOW)
