#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:52:05 2023

@author: sm

Simple click example
"""

import click

@click.command()
@click.option('--greeting', default='hiyaa', help='How do you want to greet?')
@click.option('--name', default='tammy', help='Who do you want to greet?')
def greet(greeting, name):
    print(greeting, name)
    
if __name__ == '__main__':
    greet()