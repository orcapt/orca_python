# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 08:26:09 2016

@author: SRINIVAS
"""

import wolframalpha as wa


c=wa.Client('@gmail.com')
        
res=c.query('what day is it today')
print(next(res.results).text)
 