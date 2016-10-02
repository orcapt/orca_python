# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:02:56 2016

@author: SRINIVAS
"""




import simplejson
import urllib.request.Request as ur
import urllib.request.urlopen as ure
import urllib
url = "https://www.virustotal.com/vtapi/v2/file/rescan"
parameters = {"resource": "99017f6eebbac24f351415dd410d522d, 7896b9b34bdbedbe7bdc6d446ecb09d5",
              "apikey": "069ee921004cfe52f111a8c8d382ab20cd678b902ee303b8e0b9b7aa7b9053f7"}
data = urllib.urlencode(parameters)
req = ur(url, data)
response = ure(req)
json = response.read()
print(json)