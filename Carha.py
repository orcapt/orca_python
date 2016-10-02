# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 10:09:04 2016

@author: SRINIVAS
"""
import sounddevice as sd
import numpy as np
fs= 44100
duration=4
recording = sd.rec(duration * fs, samplerate=fs, channels=2)
sd.wait()
fay=[]
way=[]

a=1
lis=[]
sil=[]
v=0

for elem in range(1,10):
    v=v+1
    print(v)
    f='Y'+str(v)+'.txt'
    a=open(f,'r')
        
    lis.append(a.readlines())
    a.close()
    f='Z'+str(v)+'.txt'
    b=open(f,'r')
    sil.append(b.readlines())
    b.close()
    
print(len(lis))
for p in range(1,fs*duration):
    fay.append(recording[p][0])
    way.append(recording[p][1])

k=-1
fr=[]
final=[]
crf=0
#fay is y

for elem in lis:
    fr=[]
    k=-1
    ray=elem
    #ray.split('\n')
    
    for ele in fay:
        k=k+1
        
        if float(ray[k])-.01<fay[k]<float(ray[k])+.01:
            fr.append('1')
            
        else:
            fr.append('0')
    final.append(fr.count('1')/len(fr))

ohh=final
k=-1
fr=[]
final=[]
crf=0
for elem in sil:
    fr=[]
    k=-1
    ray=elem
    #ray.split('\n')
    
    for ele in way:
        k=k+1
        
        if float(ray[k])-.001<fay[k]<float(ray[k])+.001:
            fr.append('1')
            
        else:
            fr.append('0')
    final.append(fr.count('1')/len(fr))

ohhh=final
print(ohh,ohhh)