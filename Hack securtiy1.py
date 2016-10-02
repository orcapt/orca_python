# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:30:25 2016

@author: SRINIVAS
"""
#069ee921004cfe52f111a8c8d382ab20cd678b902ee303b8e0b9b7aa7b9053f7

















import simplejson
import urllib
import urllib2
url = "https://www.virustotal.com/vtapi/v2/comments/put"
parameters = {"resource": "99017f6eebbac24f351415dd410d522d",
               "comment": "How to disinfect you from this file... #disinfect #zbot",
               "apikey": "069ee921004cfe52f111a8c8d382ab20cd678b902ee303b8e0b9b7aa7b9053f7"}
data = urllib.urlencode(parameters)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
json = response.read()
print(json)