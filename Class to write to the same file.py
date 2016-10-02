# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:26:11 2016

@author: SRINIVAS
"""

def Write(linenumber,file,content):
        ile=open(file,'r')
        filer=ile.readlines()
        ile.close
        file1=open(file,'w')
        linenumber=linenumber-1
        loop=-1
        for elem in filer:
            loop=loop+1
            if loop!=linenumber:
                file1.write(elem)
            else:
                file1.write(content)
def Read(linenumber,file):
          ile=open(file,'r')
          lines=ile.readlines()
          ile.close()
          return lines[linenumber-1]
v=Read(30,'Class to write to the same file.py')
Write(30,'Class to write to the same file.py',int(v)+1)
print(Read(30,'Class to write to the same file.py'))

)

25