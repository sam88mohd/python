#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:22:41 2023

@author: sm
"""

import if_example
import unittest

class Test_if_example(unittest.TestCase):
    def test_if_example(self):
        result = if_example.if_example()
        self.assertEqual(result, 100)
        
if __name__ == "__main__":
    unittest.main()