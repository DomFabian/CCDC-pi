NCCDC Escape Room
==================

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

The controller device just used DHCP. As did Dom's laptop for Bob's login. Their IPs weren't really important.

Challenges
----------

Note: the scripts expect the various state and auxiliary file to be located in the same directory, so be mindful of this when moving around or renaming files!

* Logic Puzzle (toggle switches with logic gate schematic)
    The `logic` directory contains all of the code for this puzzle. `generate_solutions.py` creates a file called `solns` used by `circuit.py`, which contains all of the possible correct answers to the puzzle. Since there are 10 switches, there are 1024 possible switch configurations of ON or OFF. Our circuit generated 4 correct solutions, in order to make the puzzle challenging enough. It is safe to tweak the logic outlined in `generate_solutions.py` so that it creates a larger or smaller solution set without affecting the performance of `circuit.py`.

* Binary Puzzle (Fibonacci numbers)
    The `binary` directory contains all of the code for this puzzle. `binary.py` is the code that actually lights up the LEDs on the board to display the Fibonacci number sequence and writes the state of the program to a file. It will loop to check if a guess has been made and then write the state accordinging. The other two files in the directory send signals to the control device based on the status written to this file and read from the guesses from the keypad. The binary puzzle code involves two Raspberry Pis: one runs the LEDs and one runs the keypad. Every incorrect guess made on the keypad triggers a "punishment video," which is a really obnoxious video that goes up on one of the large screens in the room. This punishment video is managed by the controller device.

* Pick Lock or Find Key
    This puzzle is pretty self-explanatory. The lock pick kit was "hidden" in an obvious place in the room, while the key to the lock was hidden inside Bob's tie knot. Clues were given in the room about the location of this key, but they were kept vague to encourage the use of the lock picks.

* Switchbox Puzzle (wire cutting)
    Once the lock is picked or opened, the safety switch box can be opened. Inside are 6 colorful wires with labels about what each wire signifies. On the side of the panel is the actual safety switch itself, which must be turned to ON in order for the puzzle to be solved. The code for this puzzle can be found in the `switchbox` directory. There is only one file, `switchbox.py`, which controls this puzzle. This script will continuously checks the wire configuration (cutting the green and black wires is the current solution) and writes the appropriate state to a state file. The controller device will poll for this state file.

Misc.
-----

The `controller-pc` directory has all of the scripts that handle the state information of the other devices. This machine is what controls the videos on the screen and shows a special video signifying success or failure upon completion. It also contains the keys required to SSH around the network. It is recommended that all of the Pis share the keys required to SSH to each other. This made development and testing much easier with only a limited number of monitors and peripherals.

The `motor` directory contains the code for the Pi running the fuel rod countdown clock. This is the same Pi that wears the powered HAT. Each of the 4 rods will be dropped one after the other every 15 minutes, slowly lowering for dramatic effect. Inside the tubes was simply a giant glow stick.

The `led-clock` directory contains code for a 4-digit 7-segment display that was purchased. While it was not used in our escape room, the code will run a countdown clock on the display starting at 60:00 (1 hour). This will need to be tweaked in order to keep better time. It's not accurate, but I'm sure the government will buy it.

Files `launcher.sh` and `launcher2.sh` are run by rc.local when the Pis boot for convenience.

The room in the GCSC had many screens at the front, so these were used. On one screen was a countdown timer with 1 hour on the clock. A large screen was used to show the various video clips such as the Turbo Encabulator and punishment videos. Another large screen was a mirror of Bob's computer.

Bob's computer is purely a diversion. If the login is entered correctly, then the user is met with a desktop full of executable batch files with names like "HACK01," "HACK02," etc. Each of these batch files Rick Rolled the participants on loop in fullscreen.

There is a binder that goes with the two panels built. Inside it live many of the clues about the puzzle, as well as some posters that need to be posted around the room.
