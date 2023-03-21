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

strace <./ap.py> // trace application systemcall - systemcall is the command application call to the kernel

strace -o file.strace ./ap/py // store the stdout in a file
less file.strace // shift-g to go to end of file