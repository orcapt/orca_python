# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:54:25 2016

@author: SRINIVAS
"""

from yahoo_finance import Share; print(Share(input('Company?')).get_open())
