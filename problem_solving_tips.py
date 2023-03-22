#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:01:58 2023

@author: sm
"""

PROBLEM SOLVING STEP
---------------------

1. gathering information
2. finding root cause
3. documentation
4. Long term remediation

strace <./ap.py> // trace application systemcall - systemcall is the command application call to the kernel

strace -o file.strace ./ap/py // store the stdout in a file
ltrace

less file.strace // shift-g to go to end of file

where to find log:
    linux:
        var/log/syslog
        .xsession-errors
    mac:
        Library/Logs
    windows:
        Event Viewer