# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:23:21 2016

@author: PRANAV
"""

import xlrd
my=input('hi')
pie=-1
ook=xlrd.open_workbook("trial.xls")
sheet = ook.sheet_by_index(0)
fi=len(sheet.row_values(0))

while pie<int(my):
    pie=pie+1
    print(sheet.row_values(pie))
