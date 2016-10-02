
"""
# -*- coding: utf-8 -*-
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
        file1.close()
def Read(linenumber,file):
          ile=open(file,'r')
          lines=ile.readlines()
          ile.close()
          return lines[linenumber-1]
if Read(32,'samef.py')=='#now you see me':
    Write(32,'samef.py',"#now you don't")
else:
    Write(32,'samef.py','#now you see me')




#now you see me