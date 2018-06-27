#!/usr/bin/python3

import time
import RPi.GPIO as io

io.setmode(io.BOARD)
io.setwarnings(False)

io.setup(40, io.OUT)

while True:
    print("HIGH")
    io.output(40, io.HIGH)

    time.sleep(1)

    print("LOW")
    io.output(40, io.LOW)

    time.sleep(1)
