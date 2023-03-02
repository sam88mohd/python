#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 22:50:38 2023

@author: sm

fire example
"""

import fire

class Ships():
    def sail(self):
        print("Your ship is setting sail")
        
    def list(self):
        ships = ["John", "Mary", "Alexander"]
        print("Ships: ", ", ".join(ships))

def sailors(fname, lname):
    print(f"{fname} {lname}")
    

class Cli():
    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()

if __name__ == "__main__":
    fire.Fire(Cli())