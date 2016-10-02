# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:01:58 2016

@author: SRINIVAS
"""

from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from pylab import plot, title, show , legend

#Linear regression example
# This is a very simple example of using two scipy tools
# for linear regression, polyfit and stats.linregress

#Sample data creation
#number of points
n=5
t=linspace(-5,5,n)
#parameters
a=0.8; b=-4
x=polyval([a,b],t)
x=[2,4,8,16,32]
#add some noise
xn=x+randn(n)

#Linear regressison -polyfit - polyfit can be used other orders polys
(ar,br,cr)=polyfit(t,xn,2)
xr=polyval([ar,br,cr],t)
#compute the mean square error
err=sqrt(sum((xr-xn)**2)/n)

print('Linear regression using polyfit')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, ms error= %.3f' % (a,b,ar,br,err))

#matplotlib ploting
title('Linear Regression Example')
plot(t,x,'g.--')
plot(t,xn,'k.')
plot(t,xr,'r.-')
legend(['original','plus noise', 'regression'])

show()

#Linear regression using stats.linregress
(a_s,b_s,r,tt,stderr)=stats.linregress(t,xn)
print('Linear regression using stats.linregress')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, std error= %.3f' % (a,b,a_s,b_s,stderr))