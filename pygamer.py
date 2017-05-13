#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 08:18:07 2016

@author: Pranavtadepalli
"""
import os
from subprocess import run
from subprocess import call
import subprocess
handle = subprocess.Popen('imagesnap',stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True,shell=True)
handle.stdout.read()
print(call(['imagesnap','imager'],shell=True))
"""
Popen(['/Users/Pranavtadepalli/Documents/Website/photos','imagesnap'],shell=True)
run('cd /Users/Pranavtadepalli/Documents/Website/photos')
print(os.system('imagesnap imag.jpg'))
"""