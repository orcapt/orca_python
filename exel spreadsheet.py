# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:23:37 2016

@author: PRANAV
"""

import xlwt
import xlrd

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("TestXL")
sheet1.write(1,3,4)
book.save(r"C:\Users\PRANAV\Documents\Python Scripts\el.xls")
