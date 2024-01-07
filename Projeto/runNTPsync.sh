#!/bin/bash

# Open a terminal and run monitor.py
gnome-terminal -- bash -c "python3 monitor.py; exec bash"

# Wait for 2 seconds
sleep 2

# Open a terminal and run NTPclient.py 0
gnome-terminal -- bash -c "python3 NTPclient.py 0; exec bash"

# Open a terminal and run NTPclient.py 1
gnome-terminal -- bash -c "python3 NTPclient.py 1; exec bash"