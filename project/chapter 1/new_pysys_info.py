#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 12:11:43 2023

@author: sm
"""

from pysys_info import call_df,sep
import subprocess

def temp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print("Space used in /tmp directory: \n")
    subprocess.call([tmp_usage, tmp_arg])
    
def main():
    call_df()
    sep()
    temp_space()
    
if __name__ == "__main__":
    main()