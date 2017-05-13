#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 08:09:42 2017

@author: Pranavtadepalli
"""

from imaplib import IMAP4
server = imaplib.IMAP4_SSL("imap.gmail.com", 993)
fi=open("pass.txt","r").read()
server.login('orca.pranav@gmail.com',fi )
"""
for ele in server.list()[1]: 
    if len(str(ele).split('INBOX'))==2:
        print(ele)
"""

r = server.select()
r, data = server.fetch("3:55", "(BODY[HEADER.FIELDS (SUBJECT)])")
for elem in data:
    for ele in str(elem).split("'"):
        if len(ele.split("Subject"))==2:
            print(ele[0:-8])