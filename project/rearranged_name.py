#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:30:05 2023

@author: sm
"""
import re

def rearranged_name(name):
    pattern = re.compile(r"([\w .]*), ([\w .]*)")
    result = pattern.match(name)
    return "{} {}".format(result[2], result[1])

if __name__ == "__main__":
    name = "Lovelace, Ada"
    rename = rearranged_name(name)
    print(rename)