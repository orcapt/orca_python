# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 09:31:09 2016

@author: SRINIVAS
"""
real=0
a=['one','two','three','four','five','six','seven','eight','nine',]
b=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
cor=list(range(1,1000))
def digit1(digit):#   inputs a 1 digit number and turns it into words#    
    ig1=a[digit[0]-1]
    return(ig1)
def digit2(digits):#   inputs 2 digit number and returns it in words
    dig1=digits[0]
    dig2=digits[1]
    if dig1==1:
        ig1=b[dig2]
    else:
        if dig2==0:
            ig1=c[dig1-2]
        else:
            ig1=c[dig1-2]+a[dig2-1]
    return(ig1)
def digit3(digits):#   same as digit 3 but inputs 3 digit number
    dig1=digits[0]
    dig2=digits[1]
    dig3=digits[2]
    if dig2==1:
        if dig3==0:
            ig1='ten'
        else:
            ig1=b[dig3]
    else:
        if dig3==0:
            if dig2==0:
                ig1=''
            else:
                if dig2==0:
                    ig1=a[dig3-1]
                else:
                    ig1=c[dig2-2]
        else:
            if dig2==0:
                ig1=a[dig3-1]
            else:
                ig1=c[dig2-2]+a[dig3-1]
    if ig1=='':
        return(a[dig1-1]+'hundred')
    else:
        return(a[dig1-1]+'hundredand'+ig1)
for drop in cor:
    d=str(drop)
    d=list(d)
    d=list(map(int,d))
    if len(d)==1:
        real=real+len(list(digit1(d)))
    if len(d)==2:
        real=real+len(list(digit2(d)))
    if len(d)==3:
        real=real+len(list(digit3(d)))
real=real+len(list('onethousand'))
print(real)



