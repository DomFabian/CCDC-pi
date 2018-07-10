#!/usr/bin/python3
import time
import RPi.GPIO as io

io.setmode(io.BOARD)
io.setwarnings(False)

# define the pins
# Note: wire = [RED,YLW,GRN,BLU,BLK,WHT]
wire = [11,13,15,19,21,23]
led_green = 5
led_red = 3

for w in wire:
    io.setup(w, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(led_green, io.OUT)
io.setup(led_red, io.OUT)

# wires connected: RED YLW BLU WHT
solution = '110101'

def get_wire_config(wire):
    ''' This function reads the pins connected to
        the wires the determine the wires that are
        cut and the ones that aren't. The colors are
        in this order: RED, YLW, GRN, BLU, BLK, WHT.
        A string is returned such as "001101," etc. '''
    
    ret = ''
    for w in wire:
        ret += str(io.input(w))
    print(ret)
    return ret

STATE_FILE = "/home/pi/CCDC-pi/switchbox/state.txt"

def write_state(state):
    ''' Write the value of 'state' on a line to the puzzle's state file. '''

    try:
        f = open(STATE_FILE, 'w')
        f.write(str(state) + '\n')
        f.close()
    except:
        pass

write_state('running')
io.output(led_red, io.HIGH)
io.output(led_green, io.LOW)
last_guess = "000000"
while True:
    time.sleep(1)
    guess = get_wire_config(wire)
    if guess == solution:
        io.output(led_red, io.LOW)
        io.output(led_green, io.HIGH)
        write_state('solved')
    else:
        io.output(led_red, io.HIGH)
        io.output(led_green, io.LOW)
        if guess != last_guess:
            write_state('running-{}'.format(guess))
            last_guess = guess

