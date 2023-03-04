#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 23:37:15 2023

@author: sm
"""

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://google.com")
