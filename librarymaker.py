#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:55:13 2017
def translate(sentence):
    new=[]
    sentence=sentence.split(' ')
    for elem in sentence:
        new.append(elem[1:]+elem[0]+'ay')
    new=' '.join(new)
    return new
@author: Pranavtadepalli
"""

def create(name,path_to_code,description,version,username,password,readme='',keywords=[]):
    import os
    from os.path import expanduser
    with open(path_to_code,'r') as file:
        code=file.read()
    os.system('mkdir '+name)
    with open(os.path.join(os.getcwd(),name+"/code.py"),'w') as file:
        file.write(code)
    with open(os.path.join(os.getcwd(),name+"/README.txt"),'w') as file:
        file.write(readme)
    with open(os.path.join(expanduser("~"),".pypirc"),'w') as file:
        file.write("""
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = %s
password = %s
[server-login]
username = %s
password = %s      
        """%(username,password,username,password,))
    with open(os.path.join(os.getcwd(),name+"/setup.py"),'w') as file:
        file.write("""
from setuptools import setup

setup(
      name='%s',    # This is the name of your PyPI-package.
      keywords='%s',
      version='%s',
      description='%s',
      long_description=open('README.txt').read(),
      scripts=['%s']                  # The name of your scipt, and also the command you'll be using for calling it
)
        """%(name,' '.join(keywords),version,description,'code.py'))
    
    os.system("cd "+name+";python3 setup.py register sdist upload -r https://upload.pypi.org/legacy/")