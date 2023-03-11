#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 08:02:12 2023

@author: sm
"""

import shutil
import psutil

def get_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = (du.free/du.total)*100
    return free < 75

def get_cpu_percent():
    cpu = psutil.cpu_percent(0.5)
    return cpu < 75

if not get_disk_usage("/") and not get_cpu_percent():
    print("ERROR!")
else:
    print("Everything is OK!")