# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 12:31:43 2016

@author: SRINIVAS
"""


import pyspectator.computer as p
a=p.Processor.temperature_stats
instance = p.Processor(1)  # the constructor may require some arguments

# access the property on the instance
instance.temperature_stats
print(instance)
