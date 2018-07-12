NCCDC Escape Room
==================

TODO: ADD MORE DETAILS!

Created for the champions of NCCDC, sponsored by Raytheon (R) (TM) (C).

Based on concept by Rudy in the Maryland CSI office. Someday I'll know his last name.

Code written by Dominick Fabian, Scott Harlan, and Doug Rogers.

Devices
-------

* Dell Inspiron mini PC (or any other machine, really)- control machine 

* Raspberry Pi 3 Model B `pi10` - fuel rod countdown timer with 4 motors  (used RPi HAT as well)

* Raspberry Pi 3 Model B `pi11` - logic puzzle and binary (Fibonacci) puzzle

* Raspberry Pi 3 Model B `pi12` - switchbox puzzle (wiring inside knife switchbox)

* Raspberry Pi 3 Model B `pi13` - keypad reader (sends entry to pi11)

* Another Windows machine - decoy machine belonging to "Bob" for participants to attempt to log into

For this build, we probably used more Raspberry Pis than we needed to. Each one has 24 useable GPIO pins, so having 4 made life a little easier. Note that `pi10` used a HAT device with a separate power supply in order to run the motors without drawing too much current from the Pi. The two non-Pi computers can be substituted for anything with a wireless NIC, an SSH client, and login screensaver.

Networking
----------

We used a wireless AP to connect all of the devices and minimize wires exposed to the participants. Here is the breakdown:

|Device|Ethernet   |Wifi        |
|------|-----------|------------|
|pi10  |10.10.10.10|192.168.1.10|
|pi11  |10.10.10.11|192.168.1.11|
|pi12  |10.10.10.12|192.168.1.12|
|pi13  |10.10.10.13|192.168.1.13|

Controller device just used DHCP. As did Dom's laptop for Bob's login. Their IPs weren't really important.

Challenges
----------

* Logic Puzzle (toggle switches with logic gate schematic)

* Binary Puzzle (Fibonacci)

* Pick Lock or Find Key

* Switchbox Puzzle (after picking lock)

