# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:08:28 2016

@author: me he 

"""

import smtplib
from email.mime.text import MIMEText
gi=input('Message?')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("Email Address", "password")
msg = gi
server.sendmail("email address", "@gmail.com", msg)

