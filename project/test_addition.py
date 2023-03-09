#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:08:49 2023

@author: sm
"""

import arithmetic
import unittest

class Test_addition(unittest.TestCase):
    # test Integer
    def test_integer(self):
        sum = arithmetic.add_numbers(50, 50)
        self.assertEqual(sum, 100)
        
    # test Float
    def test_float(self):
        sum = arithmetic.add_numbers(50.6, 10.0)
        self.assertEqual(sum, 60.6)
        
    # test String
    def test_number_string(self):
        sum = arithmetic.add_numbers("hello", "world")
        self.assertEqual(sum, "helloworld")
        
if __name__ == "__main__":
    unittest.main()