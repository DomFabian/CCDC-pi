#!/usr/bin/python3

import time
import RPi.GPIO as io

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


def write_binary(num, bit):
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

def is_correct_solution():
    ''' When sending the solution guesses to this Pi,
        another host will send a file over a network
        to this Pi via SCP. This function checks to see
        if that file exists. If it does exist, this is
        interpretted as having the correct solution entered
        on the other host and the function returns True.
        Otherwise, the puzzle has not yet been solved and
        the function returns False. '''

    filename = '/home/pi/CCDC-pi/binary/binary_soln'

    try:
        f = open(filename, 'r')
        return True
    except:
        return False
    

fibonacci = ['00000000', '00000001', '00000001', '00000010', '00000011', '00000101', '00001000',
             '00001101', '00010101', '00100010', '00110111', '01011001', '10010000', '11101001']

write_binary('00000000', bit)
io.output(led_red, io.HIGH)
io.output(led_green, io.LOW)
flag = False
while not flag:
    for num in fibonacci:
        if is_correct_solution():
            flag = True
            break
        write_binary(num, bit)
        time.sleep(2)
        write_binary('00000000', bit)
        time.sleep(1)
    time.sleep(2)

write_binary('11111111', bit)
io.output(led_green, io.HIGH)
io.output(led_red, io.LOW)

