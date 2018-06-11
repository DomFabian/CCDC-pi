import time
import RPi.GPIO as io

io.setmode(io.BOARD)

# define some pins
led_red = 11
led_yellow = 13
led_green = 15
switch1 = 7


io.setup(
