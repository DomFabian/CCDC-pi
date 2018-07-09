#!/usr/bin/python3

import time
import RPi.GPIO as io
import subprocess

io.setmode(io.BOARD)
io.setwarnings(False)

# define the pins
## yeah, I use 1 letter variable names
A = 37
B = 35
C = 33
D = 31
E = 29
F = 23
G = 21
colon_ground = 26
colon = 8
dec = 19

## digits index from 0 (leftmost) to 3 (rightmost)
digit = [40, 38, 36, 32]

# set up the pins
io.setup(A, io.OUT)
io.setup(B, io.OUT)
io.setup(C, io.OUT)
io.setup(D, io.OUT)
io.setup(E, io.OUT)
io.setup(F, io.OUT)
io.setup(G, io.OUT)
io.setup(colon_ground, io.OUT)
io.setup(colon, io.OUT)
io.setup(dec, io.OUT)

for d in digit:
    io.setup(d, io.OUT)


def write_digit(dig):
    ''' This function takes a integer digit
        and writes it to all of the digit
        displays on the LED board. '''

    dig = int(dig)
    
    pins = [A,B,C,D,E,F,G]
    on = []
    off = []
    if dig == 0:
        on.extend([A,B,C,D,E,F])
        off.extend([G])
    elif dig == 1:
        on.extend([B,C])
        off.extend([A,D,E,F,G])
    elif dig == 2:
        on.extend([A,B,G,E,D])
        off.extend([F,C])
    elif dig == 3:
        on.extend([A,B,G,C,D])
        off.extend([F,E])
    elif dig == 4:
        on.extend([F,B,G,C])
        off.extend([A,E,D])
    elif dig == 5:
        on.extend([A,F,G,C,D])
        off.extend([B,E])
    elif dig == 6:
        on.extend([A,F,E,D,C,G])
        off.extend([B])
    elif dig == 7:
        on.extend([A,B,C])
        off.extend([F,G,E,D])
    elif dig == 8:
        on.extend([A,B,C,D,E,F,G])
    elif dig == 9:
        on.extend([A,B,C,D,F,G])
        off.extend([E])
    else:
        return

    for o in on:
        io.output(o, io.HIGH)
    for o in off:
        io.output(o, io.LOW)


def select_digit(dig):
    ''' This function sets the digit that is ON
        on the LED display. Only one should be ON
        at a time. Parameter `dig` is the index
        of the digit that should be ON. '''

    dig = int(dig)
    if dig > 3 or dig < 0:
        return

    for d in digit:
        io.output(d, io.HIGH)
    io.output(digit[dig], io.LOW)

def write_time(t, sleep_time):
    ''' This function takes an INTEGER time in
        seconds and displays it on the LED
        display. `sleep_time` is taken only for
        consistency in timing. '''

    t = int(t)

    mins = int(t / 60)
    secs = t % 60

    if mins < 10:
        mins = '0' + str(mins)
    else:
        mins = str(mins)
    if secs < 10:
        secs = '0' + str(secs)
    else:
        secs = str(secs)

    # `cycles` should be tweaked to make each time appear
    # for only one second
    cycles = 100
    
    for i in range(0, cycles):
        select_digit(0)
        write_digit(int(mins[0]))
        time.sleep(sleep_time)
        select_digit(1)
        write_digit(int(mins[1]))
        time.sleep(sleep_time)
        select_digit(2)
        write_digit(int(secs[0]))
        time.sleep(sleep_time)
        select_digit(3)
        write_digit(int(secs[1]))
        time.sleep(sleep_time)

def hold_zero(sleep_time):
    while True:
        for i in range(0, 4):
            select_digit(i)
            write_digit(0)
            time.sleep(sleep_time)
    
    
#--------------------------------------------------------
io.output(A, io.LOW)
io.output(B, io.LOW)
io.output(C, io.LOW)
io.output(D, io.LOW)
io.output(E, io.LOW)
io.output(F, io.LOW)
io.output(G, io.LOW)
io.output(colon_ground, io.LOW)
io.output(colon, io.HIGH)
io.output(dec, io.LOW)
for d in digit:
    io.output(d, io.HIGH)


sleep_time = 0.0025
seconds = 3600

for i in range(seconds, 0, -1):
    write_time(i, sleep_time)

hold_zero(sleep_time)
    


