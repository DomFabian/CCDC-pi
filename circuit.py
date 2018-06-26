import time
import RPi.GPIO as io

io.setmode(io.BOARD)
io.setwarnings(False)

# define the pins
led_green = 5
led_yellow = 3
led_red = 7

switch = [11,13,15,19,21,23,29,31,33,35]

io.setup(led_green, io.OUT)
io.setup(led_yellow, io.OUT)
io.setup(led_red, io.OUT)

for s in switch:
    io.setup(s, io.IN)

# read from the solution file
filename = 'solns'

solutions = []

def get_switch_config(switch):
    ''' This function gets the current switch configuartion
    and returns it as a string of 0s and 1s. switch arg is
    the list of switch pin numbers.
    Exp: 0101101001, 0000000000, etc. '''
    
    ret = ''
    for s in switch:
        ret += str(io.input(s))
    return ret

print(get_switch_config(switch))

def is_valid_config(config, solutions):
    ''' This function takes the current switch config as a
        string and the list of solutions (also strings) and
        returns a Boolean of if the current config is in the
        solution set. '''
    
    if not config or not solutions:
        return False

    for sol in solutions:
        if config == sol:
            return True
    return False

while True:
    
    
    
    sleep(2)
