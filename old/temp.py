# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import matplotlib.pylab as plt

os.chdir('C:/Users/Natna/Downloads/enron_mail_20150507.tar/maildir')
file=os.listdir('.')
d = {}
x=0
y=0
#line=file.readline()
while x < len(file):
    
    line= file[x]
    
    name=os.listdir(line)
    #  os.path.isdir(line+'/inboxadfad'
    if (os.path.isdir(line+'/_sent_mail')):
        
        inbox=os.listdir(line + '/_sent_mail')
    
        subject=line
        d[line]=len(inbox)
        x=x+1
    else:
        y=y+1
        x=x+1
lists=sorted(d.items())

d_inbox = d
b,d=zip(*lists)
xvalue = range(len(b))
plt.plot(xvalue,d)

plt.show
'''allenp = os.listdir('allen-p/')


inbox = os.listdir('allen-p/inbox')

d = {}
d['allenp'] = len(inbox)'''
