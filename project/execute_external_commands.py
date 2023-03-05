#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:53:25 2023

@author: sm
"""
import subprocess

subprocess.call(["touch", "sample.txt"])
subprocess.call(["ls", "-la"])
print("sample.txt created")
subprocess.call(["rm", "sample.txt"])

subprocess.call(["ls", "-la"])
print("sample.txt deleted")

