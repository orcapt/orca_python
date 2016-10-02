# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:36:39 2016

@author: PRANAV
"""
import email
twi=0
import pyzmail
import re
import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('Email address', 'password')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox")
result, data = mail.search(None, "ALL")
 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
 
result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads
#print(raw_email)
#print(pyzmail.decode_text(raw_email,'',''))
#maw=pyzmail.message_from_string(str(raw_email))
maw=pyzmail.message_from_bytes(raw_email)
print(maw)
email_message = email.message_from_string(str(raw_email))
hi=email_message.items()
hi=hi[0]
hi=hi[1]
hi=str(hi).split(' ')
#print(hi)
for elem in hi:
    if twi!=0:
        print(elem)
        twi=twi-1
    if len(elem)!=0:
        hie=elem.split('\\')
        if hie[-1]=='nSubject:':
            twi=10

    