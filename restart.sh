#!/bin/sh
#
# designed to be run from working directory of clock.py
#
#export DISPLAY=:0.0
#
# kill any processes matching clock.py
kill $(pgrep -f clock.py)

# wait 1 second
sleep 1

# restart process
python3 clock.py &
