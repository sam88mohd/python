#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:51:04 2023

@author: sm

input by pipe

echo -e '15\n12\n2' | python input_by_pipe.py
"""

import sys

for n in sys.stdin:
    print (int(n.strip())// 2)
    

