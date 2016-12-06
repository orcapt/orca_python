# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:35:20 2016

@author: SRINIVAS
"""
from bs4 import BeautifulSoup as soup
import re
import webbrowser
import urllib.request
from pytrends.request import TrendReq
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import time
import speech_recognition as sr
class wordinfo:
    definition='pi'
    def __init__(self,word):
        self.word=word
        try:
            import urllib.request as lib
            from bs4 import BeautifulSoup as soup
            raw=lib.urlopen('http://www.merriam-webster.com/dictionary/'+self.word).read()
            raw=soup(raw,'lxml')
            raw1=lib.urlopen('http://www.dictionary.com/browse/'+self.word).read()
            tre=soup(raw1,'lxml')
            self.tre=tre
            #self.raw=raw
            #print(soup.find_all(name="keywords"))
            self.raw=raw
            self.lib=lib
            self.soup=soup
        except IndexError:
            print('You need to install bs4 and/or urllib.request')
    def definition(self):
        #raw=self.lib.urlopen('http://www.merriam-webster.com/dictionary/'+self.word).read()
        #aw=self.soup(raw,'lxml')
        #print(raw.find_all('meta')[-2])
        defin=self.raw.find_all(class_="definition-inner-item with-sense")
        ft=[e.get_text() for e in defin]
        definition=[]
        for elem in ft:
            definition.append(elem[1:].replace(u'\xa0', u' '))
        return(definition)
    def pos(self):
        os=self.raw.find_all(class_='main-attr')
        os=list(set([e.get_text().strip(' ') for e in os]))
        return(os)
    def origin(self):
        tre=self.tre.find_all(class_='def-set')
        #print(tre)
        
        loop=-1
        for elem in tre:
            loop=loop+1
            elem=str(elem)
            try:
                #print(elem.split('</p>'))
                if len(elem.split('</p>'))!=1:
                    origin=elem
                    tre.pop(loop)
                    
            except:
                pass
        
        origin=''.join(self.soup(origin,'lxml').get_text().split('\n'))
        return(origin)
    def synonyms(self):
        raw=self.lib.urlopen('http://www.thesaurus.com/browse/'+self.word).read()
        raw=self.soup(raw,'lxml')
        pr=[e.get_text().replace('\n',' ').replace('  ','').strip('\n').split('star') for e in raw.find_all(class_='relevancy-list')]
        rp=[]
        for elem in pr:
            for t in elem:
                if t!='':
                    rp.append(t)
        return(rp)
    def antonyms(self):
        raw=self.lib.urlopen('http://www.thesaurus.com/browse/'+self.word).read()
        raw=self.soup(raw,'lxml')
        pr=[e.get_text().replace('\n',' ').replace('  ','').strip('\n').split('star') for e in raw.find_all(class_='list-holder')]
        rp=[]
        for elem in pr:
            for t in elem:
                if t!='':
                    if ' ' in list(t):
                        for lem in t.split(' '):
                            rp.append(lem)
                    else:
                        rp.append(t)
        return(rp)
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
    pier=wordinfo(elem)
    pier=pier.pos()
    if 'noun' in str(pier):
#        if len(pier)<3:
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
    #print(000)
    time.sleep(4)
rfe.close()
print('Your sentence is ',real.count(1)/len(real)*100, '%', 'thanksgiving related')




for el in sent:
    in1=el
    raw=urllib.request.urlopen('http://www.bing.com/images/search?q='+in1+'&view=detail&first=1').read()
    raw=soup(raw)
    orca=raw.find_all('img')[5:-1]
    urls=[]
    for tag in orca:
        value = tag["src"]
        urls.append(value)
    
    
file=open('ih.html','w')
file.write("""
<!doctype html>
<html>
<body>
""")
file.write('<h1>'+str(real.count(1)/len(real)*100)+'% thankgiving'+'</h1>')
file.write('\n')
fier=0
pile=len(urls)
for elem in urls:
    file.write(r'<img src="'+elem+'">')
    file.write('\n')
file.write("""
</body>
</html>
""")
file.close()
ber=webbrowser.get('windows-default')
ber.open(r"file:\\\Users\PRANAV\Documents\Python Scripts"+r'\ih.html')