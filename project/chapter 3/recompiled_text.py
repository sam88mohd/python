#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:35:37 2023

@author: sm
"""
import re

def run_re():
    pattern = "pDq"
    
    infile = open("sample-2mb-text-file.txt", 'r')
    lines = 0
    match_count = 0
    for line in infile:
        match = re.search(pattern, line)
        if match:
            match_count += 1
        lines += 1
    return (lines, match_count)

if __name__ == '__main__':
    lines, match_count = run_re()
    print("LINES::", lines)
    print("MATCHES::", match_count)
        
    