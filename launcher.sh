#!/bin/bash

# set up networking
sudo ifconfig eth0 10.10.10.11 up

python3 /home/pi/CCDC-pi/logic/generate_solutions.py &

python3 /home/pi/CCDC-pi/logic/circuit.py &

python3 /home/pi/CCDC-pi/binary/binary.py
