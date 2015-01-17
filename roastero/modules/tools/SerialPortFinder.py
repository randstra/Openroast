#!/usr/bin/env python
# Name: SerialPortFinder.py
# Authors: Mark Spicer, Caleb Coffie
# Purpose: Return the serial port url when given a VID:PID

from serial.tools import list_ports
import re

def vid_pid_to_serial_url(vidpid):
    #Get all com ports currently connected to the system
    currentComPorts = list(list_ports.comports())
    for port in currentComPorts:
        if re.search(vidpid, port[2], flags=re.IGNORECASE):
            return port[0]
    raise LookupError('VID:PID Not found on system')
