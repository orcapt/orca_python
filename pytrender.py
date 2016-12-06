# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:17:59 2016

@author: SRINIVAS
"""

from pytrends.request import TrendReq
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import time
import speech_recognition as sr

rfe=open('thanks.txt','r')
time.sleep(1)
r = sr.Recognizer()

try:
    with sr.Microphone() as source:                # use the default microphone as the audio source
                audio = r.listen(source)
                
                sentence=r.recognize_google(audio)
                print('I heard that you said:\n',sentence)
except:
    sentence=input('Enter a sentence (we could not figure out what you said)')
google_username = "username@gmail.com"
google_password = "password"
path = ""

sent=[]
for elem in sentence.split(' '):
    pier=dictionary.meaning(elem)
    if 'Noun' in str(pier):
        if len(pier)==1:
            sent.append(elem)
pie=[]
real=[]
loopy=0
tea=[]
if len(sent)>3:
    for elem in sent:
        loopy=loopy+1
        tea.append(elem)
        if loopy==3:
            loopy=0
            pie.append(','.join(tea))
            tea=[]
else:
    pie.append(','.join(sent))
if tea!=[]:
    pie.append(','.join(tea))
print(pie)
for elem in pie:
    if elem in rfe.read().split('\n'):
        real.append(1)
# connect to Google
pytrend = TrendReq(google_username, google_password, custom_useragent='My Pytrends Script')
for load in pie:
#load='thanksgiving,soccer,soccer'
    length=len(load.split(','))
    listy=[]
    for elem in range(length):
        exec('c'+str(elem)+'=0')
    for elem in range(length):
        exec('d'+str(elem)+'=0')
    trend_payload = {'q': load}
    
    # trend
    trend = pytrend.trend(trend_payload)
    #print(trend)
    df = pytrend.trend(trend_payload, return_type='dataframe')
    df=str(df)
    df=str(df).split('\n')
    fd=[x[5:-1] for x in df]
    words=df[0].strip(' ').split('  ')
    a=0
    a1=0
    
    for elem in fd[1:]:
        if elem[0:2]=='11':
            horn=-1
            a1=a1+1
            #print(elem)
            er=elem[7:]
            er=er.split(' ')
            er=[x for x in er if x!='']
            #print(er)
            for l in er:
                try:
                    horn=horn+1
                    exec('d'+str(horn)+'=d'+str(horn)+'+'+l)
                except:
                    pass
        else:
            a=a+1
            porg=-1
            #print('a',elem)
            er=elem[7:]
            er=er.split(' ')
            er=[x for x in er if x!='']
            #print('a',er)
            
            for l in er:
                try:
                    #print(0)
                    porg=porg+1
                    #print(eval('c'+str(porg)),'\n')
                    exec('c'+str(porg)+'=c'+str(porg)+'+'+l)
                except:
                    pass
    no=[]  
    yes=[]     
    #print(eval('c0'),'a' )    
    for l in range(length):
        #print(eval('c'+str(l)))
        no.append(eval('c'+str(l))/a)
    for l in range(length):
        yes.append(eval('d'+str(l))/a1)
    #print(yes)
    #print(no)

    loop=-1
    for elem in yes:
        loop=loop+1
        if elem>(no[loop]+5):
            real.append(1)
        else:
            real.append(0)
    

    yes=[]
    no=[]
    print(000)
    time.sleep(4)
rfe.close()
print('Your sentence is ',real.count(1)/len(real)*100, '%', 'thanksgiving related')