#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:22:15 2017

@author: Pranavtadepalli
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:16:33 2017

@author: Pranavtadepalli
"""
#'"id","qid1","qid2","question1","question2","is_duplicate"'
import csv
from fuzzywuzzy import fuzz
from stop_words import get_stop_words
stopwords=get_stop_words('en')
def function1(q1,q2):
    if fuzz.ratio(q1, q2)>50:
        return 1
    else:
        return 0
def function(q1,q2):
    q1=' '.join([q for q in q1.split(' ') if q not in stopwords])
    q2=' '.join([q for q in q2.split(' ') if q not in stopwords])
    try:
        if fuzz.ratio(q1, q2)>58:
            return 1
        else:
            return 0
    except:
        return 0

final=open('submission25.csv','a')
final.write("test_id,is_duplicate\n") 
time=1
with open('test-3.csv', newline='\n',encoding='UTF-8') as f:
    reader = csv.reader(f)
    for elem in reader:
        if time==0:
            result=function(elem[1],elem[2])
            final.write(elem[0])
            final.write(','+str(result)+'\n')
        else:
            time=0
final.close()