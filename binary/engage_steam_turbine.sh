#!/bin/bash

echo ""
echo "Use Ctrl-C to exit."
echo ""

while [ -t ]; do
    read -p 'Enter final Steam Turbine Engagement code: ' code
    if [ -n "$code" ]; then
	code=$(printf "%u" "$code" 2> /dev/null)
	if [ $? -ne 0 ]; then
	    echo "Really?"
	else
	    echo "Sending '$code'."
	    ssh pi11 echo "$code" '>' /home/pi/CCDC-pi/binary/binary_soln
	fi
    fi
done

exit 0
