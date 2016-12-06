# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:48:50 2016

@author: SRINIVAS
"""

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
        

word=wordinfo('bannanas')

print(word.synonyms())
print(word.antonyms())
print(word.definition())
#relevancy-list