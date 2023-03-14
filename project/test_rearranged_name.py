#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:11:45 2023

@author: sm
"""

from rearranged_name import rearranged_name
import unittest

class TestRearrangeName(unittest.TestCase):
    def test_normal(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearranged_name(testcase), expected)
        
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearranged_name(testcase), expected)
        
    def test_double_name(self):
        testcase = "Kennedy, John F."
        expected = "John F. Kennedy"
        self.assertEqual(rearranged_name(testcase), expected)
        
    def test_single_name(self):
        testcase = "Volatile"
        expected = "Volatile"
        self.assertEqual(rearranged_name(testcase), expected)
if __name__ == "__main__":
    unittest.main()