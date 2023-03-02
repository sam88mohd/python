#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 12:23:03 2023

@author: sm
"""

import subprocess, platform

def checking_server(ping_ip):
    ping_cmd = f"ping {'-n' if platform.system().lower() == 'windows' else '-c'} 5 "
    usr = "root"
    print(f"checking server ({ping_ip}) availability. Please wait...\n")
    try:
        subprocess.check_output(ping_cmd + ping_ip, shell=True)
        print(f"Server {ping_ip} is available. connecting to the server now")
        subprocess.call(["ssh", usr + "@" + ping_ip])
    except Exception:
        print(f"Server {ping_ip} is not available!")
    

def main():
    ping_ip = "192.168.0.2"
    checking_server(ping_ip)
    
if __name__ == '__main__':
    main()