#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:44:47 2023

@author: sm
"""

def decorator_function(wrapped_function):
    def wrapper():
        print("run before wrapped function")
        wrapped_function()
        print("run after wrapped function")
    return wrapper

@decorator_function
def foobar():
    print("foobar")
    
# no need if using decorator
# f = decorator_function(foobar)

if __name__ == "__main__":
    
    foobar()