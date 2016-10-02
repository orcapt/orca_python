# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 19:33:03 2016

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
    def text(self,string,tags):
        strings=[]
        loop=-1
        for tag in tags:
            loop=loop+1
            strings.append('<'+tag+'>')
            strings.append(string[loop])
        #strings.append(string[loop+1])
        for tag in list(reversed(tags)):
            loop=loop+1
            strings.append('</'+tag+'>')
            try:
                strings.append(string[loop])
            except IndexError:
                pass
        print(''.join(strings))
        self.file.write(''.join(strings))
    def image(self,url):

        self.file.write(r'<img src="'+url+'">')
    def button(self,text):
        self.file.write('<button type="button">'+text+'</button>')
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
html.text(['1','2','1','2','1'],['small','mark','small'])
a=[':sub:',[':bold:',':mark:','i like red',[':sub:','milk']]]
html.text('1',['h2'])
html.close()
html.show()