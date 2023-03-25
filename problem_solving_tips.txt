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
        
1.creating a reproduction case
2. finding root cause

test our hypotesis in test envionment - include set up new test server, test data and so on

iotop - use to check input output process.
iostat , vmstat - show statistic on the io operation
ionice - use to configure io resources
iftop - show current traffic process

rsync - backup software - us bwlimit to limit bw used
Trickle - set bw limit

nice - reduce priority of process using CPU

head -20 // print first 20 line

tail -5 // print last 5 line

wc -l <file>// print how many line for the file