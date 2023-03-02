#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:45:38 2023

@author: sm
"""

import re, io

vhost_start = re.compile(r'<VirtualHost\s(.*?)>')
vhost_end = re.compile(r'<\/VirtualHost>')
docroot_re = re.compile(r'DocumentRoot\s(.*?)(\S+)')

def replace_docroot(conf_string, vhost, new_docroot):
    curr_vhost = None
    in_vhost = False
    conf_file = io.StringIO(conf_string)
    for line in conf_file:
        vhost_start_match = vhost_start.match(line)
        if vhost_start_match:
            curr_vhost = vhost_start_match.group()[0]
            in_vhost = True
        if in_vhost and (curr_vhost == vhost):
            docroot_match = docroot_re.match(line)
            if docroot_match:
                sub_line = docroot_re.sub(r'\1$s' %new_docroot, line)
                line = sub_line
        vhost_end_match = vhost_end.match(line)
        if vhost_end_match:
            in_vhost = False
        yield line
        
        
if __name__ == '__main__':
    conf_file_path = 'config.xml'
    vhost = 'local2:80'
    new_docroot = '/tmp'
    conf_string = open(conf_file_path, 'r').read()
    for line in replace_docroot(conf_string, vhost, new_docroot):
        print(line)