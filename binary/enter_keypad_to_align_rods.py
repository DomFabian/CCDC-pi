#!/usr/bin/python

import RPi.GPIO as GPIO
import subprocess
import sys
import time

ENABLE_OUTPUT = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(ENABLE_OUTPUT)
 
class keypad():
    def __init__(self, columnCount = 3):
        GPIO.setmode(GPIO.BOARD)

        # CONSTANTS 
        if columnCount is 3:
            self.KEYPAD = [
                ["1","2","3"],
                ["4","5","6"],
                ["7","8","9"],
                ["*","0","#"]
            ]

            self.ROW         = [12, 16, 18, 22] # BCM: [18,23,24,25]
            self.COLUMN      = [7, 11, 15]      # BCM: [4,17,22]

        elif columnCount is 4:
            self.KEYPAD = [
                ["1","2","3","A"],
                ["4","5","6","B"],
                ["7","8","9","C"],
                ["*","0","#","D"]
            ]

            self.ROW         = [12, 16, 18, 22] # BCM: [18,23,24,25]
            self.COLUMN      = [7, 11, 15, 40]  # BCM: [4,17,22,21]
        else:
            return
     
    def getKey(self):
         
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
         
        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i
                 
        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
        if rowVal <0 or rowVal >3:
            self.exit()
            return
         
        # Convert columns to input
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
         
        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)
 
        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
                 
        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if colVal <0 or colVal >2:
            self.exit()
            return
 
        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[rowVal][colVal]
         
    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def debounceKey():
    r = None
    while r == None:
        r = kp.getKey()
    none_count = 0
    while none_count < 3:
        if kp.getKey() == None:
            none_count += 1
            time.sleep(0.01)
        else:
            none_count = 0
    return r

def key_delay():
    # time.sleep(0.25)
    pass

def dprint(s, opt=None):
    if ENABLE_OUTPUT:
        if opt is not None:
            print(s, opt)
        else:
            print(s)

def write_flush(s):
    if ENABLE_OUTPUT:
        sys.stdout.write(s)
        sys.stdout.flush()
        
if __name__ == '__main__':
    # None of the output will be seen:
    dprint("")
    dprint("Use Ctrl-C to exit.")
    dprint("")

    # Initialize the keypad class
    kp = keypad()

    while True:
        write_flush('Enter final Control/Fuel Rod Alignment code: ')
        entry = ''
        while True:
            d = debounceKey()
            # print("type(d)=" + str(type(d)) + " d='" + d + "'")
            if d == '*':
                key_delay()
                continue
            if d == '#':
                write_flush('\n')
                key_delay()
                break
            write_flush(d)
            entry = entry + d
            key_delay()
        arg_list = [
            "/usr/bin/ssh",
            "pi11",
            "echo " + entry,
            ">",
            "/home/pi/CCDC-pi/binary/binary_soln"
        ]
        dprint("Sending: '{}'...".format(entry))
        dprint("arg_list = " + str(arg_list))
        subprocess.call(arg_list)

