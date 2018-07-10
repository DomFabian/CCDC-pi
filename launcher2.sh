#!/bin/bash

# this launcher is for the Pi that controls the wires puzzle ONLY

# set up networking
sudo ifconfig eth0 10.10.10.12 up

python3 /home/pi/CCDC-pi/switchbox/switchbox.py

exit 0
