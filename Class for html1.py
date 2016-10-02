# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 13:10:32 2016

@author: SRINIVAS
"""

import webbrowser
class html:
    def openfile(self):
        file=open('its.html','w')
        self.file=file
        self.file.write('<!doctype html>')
        self.file.write('\n')
        self.file.write('<html>')
        self.file.write('\n')
        self.file.write('<body>')
        self.file.write('\n')
    """
    def openfunction(self,name,arguments):
        arguments=','.join(arguments)
        self.file.write('<script type="text/javascript">')
        self.file.write('\n')
        self.file.write('function '+name+'('+arguments+')'+'\n'+'{'+'\n')
    def contentfunction(self):
        alert(clicked_id);
        }
        </script>
    """
    def text(self,a):

        listy=[]
        for elem in str(a).split(" "):
            if elem[-1]==':':
                listy.append('<'+elem[0:-1]+'>')
            elif elem[0]==':':
                listy.append('</'+elem[1:]+'>')
            else:
                listy.append(elem)
        the=''.join(listy)
        self.file.write(the)
    def image(self,url,h='',w='',alt='sorry this image can not be displayed'):
        if h=='' and w=='':
            self.file.write(r'<img src="'+url+'">')
        if h=='' and w!='':
            self.file.write(r'<img width="'+str(w)+'" src="'+url+'">')
        if h!='' and w=='':
            self.file.write(r'<img height="'+str(h)+'" src="'+url+'">')
        if h!='' and w!='':
            self.file.write(r'<img height="'+str(h)+' width="'+str(w)+'" src="'+url+'">')
    def button(self,text):
        self.file.write('<button type="button">'+text+'</button>')
    def newcontainer(self,name,height,width,direction,backcolor='#eee',):
        self.container+name='<div style="background-color:'+backcolor+';height:'+height+'px;width:'+width+'px;float:'+direction+';">'
    def writecontainer(self,name):
        name='container'+name
        a='/n'
    def close(self):
        self.file.write('</body>')
        self.file.write('\n')
        self.file.write('</html>')
        self.file.write('\n')
        self.file.close()
    def show(self):
        ber=webbrowser.get('windows-default')
        ber.open(r"C:\Users\SRINIVAS\Documents\Python Scripts"+r'\its.html')
"""
    file.write('<html>')
    file.write('\n')
    file.write('<body>')
    file.write('\n')
    file.write('<h1>'+str.upper(input1)+'</h1>')
    file.write('\n')
"""











html=html()
html.openfile()
html.text('small: hi :small')
html.image('http://test.scripts.psu.edu/users/j/u/jul229/mini.jpg')
html.close()
html.show()