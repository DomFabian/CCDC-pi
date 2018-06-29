#!/usr/bin/python3
import time
import RPi.GPIO as io

io.setmode(io.BOARD)
io.setwarnings(False)

# define the pins
# Note: wire = [RED,YLW,GRN,BLU,BLK,WHT]
wire = [11,13,15,19,21,23]
led_gree = 5
led_red = 7

for w in wire:
    io.setup(w, io.IN, pull_up_down=io.PUD_DOWN)
io.setup(led_green, io.OUT)
io.setup(led_red, io.OUT)

solution = [1,1,1,1,1,1]

def get_wire_config(wire):
    ''' This function reads the pins connected to
        the wires the determine the wires that are
        cut and the ones that aren't. The colors are
        in this order: RED, YLW, GRN, BLU, BLK, WHT.
        A string is returned such as "001101," etc. '''
    
    ret = ''
    for w in wire:
        ret += io.input(w)

    return ret

while True:
    if
