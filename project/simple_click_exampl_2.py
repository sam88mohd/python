#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:18:08 2023

@author: sm

simple_click_example_2
"""

import click

@click.command()
@click.option('--greeting', default="hiya", help="How do you want to greet?")
@click.option('--name', default="John", help="How do you want to name?")
def show_greeting(greeting, name):
    print(f"{greeting}, {name}")
    
if __name__ == '__main__':
    show_greeting()