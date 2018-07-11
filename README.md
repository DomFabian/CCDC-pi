NCCDC Escape Room
==================

TODO: ADD MORE DETAILS!

Created for the champions of NCCDC, sponsored by Raytheon (R) (TM) (c).

Based on concept by Rudy in the Maryland CSI office. Someday I'll know his last name.

Code written by Dominick Fabian, Scott Harlan and Doug Rogers.

Devices
-------

#. Control machine (we used a Dell Inspiron mini PC)

#. Raspberry pi10 - fuel rod timer with 4 motors

#. Raspberry pi11 - logic puzzle and binary (Fibonacci) puzzle

#. Raspberry pi12 - switchbox puzzle (wiring inside knife switchbox)

#. Raspberry pi13 - keypad reader - sends entry to pi11

Networking
----------

|Device|Ethernet   |Wifi        |
|------|-----------|------------|
|pi10  |10.10.10.10|192.168.1.10|
|pi11  |10.10.10.11|192.168.1.11|
|pi12  |10.10.10.12|192.168.1.12|
|pi13  |10.10.10.13|192.168.1.13|

Controller device just used DHCP. As did Dom's laptop for Bob's login.

Challenges
----------

#. Logic Puzzle (toggle switches with logic gate schematic)

#. Binary Puzzle (Fibonacci)

#. Pick Lock or Find Key

#. Switchbox Puzzle (after picking lock)

