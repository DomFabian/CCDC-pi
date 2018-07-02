#!/bin/bash

# This script will send the file indicating that the binary
# sequence puzzle has been solved. The following network is 
# assumed:
## 10.10.10.10: motor-driving Raspberry Pi
## 10.10.10.11: logic puzzle/binary sequence Raspberry Pi

sshpass -f "/home/pi/CCDC-pi/key" ssh 10.10.10.11 touch /home/pi/CCDC-pi/binary/binary_soln

exit 0