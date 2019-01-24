# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:40:52 2018

@author: Natna
"""
import os
import networkx as nx
from networkx.algorithms import community 
os.chdir('C:/Users/Natna/Downloads/enron_mail_20150507.tar/maildir/')
G=nx.path_graph(10)
co=community.k_clique_communities
x=0
y=0
i=0
larg_pair=[]
t=3
file=os.listdir('.')
while x < len(file):
    
    line= file[x]
    
    name=os.listdir(line)
    #  os.path.isdir(line+'/inboxadfad'
    if (os.path.isdir(line+'/inbox')):
        
        inbox=os.listdir(line + '/inbox')
        while i<len(inbox):
            pairs=[]
            if(os.path.isfile(line+'/inbox'+"/"+inbox[i])):
                with open(os.path.join(line+'/inbox',inbox[i]),'r') as f:
            
                    f_contents=f.readlines()
                   # if(f_contents[3][:2]=='To'):
                    p=0
                    pairs.append(f_contents[2])
                    r=3
            while(not("Subject:" in f_contents[r])):
                    
                   
                    pairs.append(f_contents[r])
                    
                    
                    larg_pair.append(pairs)
                    subject=line
                    i=i+1
                    p=p+1
                    r=r+1
            
                   # else:
                        
                    #    i=i+1
            else:
                i=i+1
        
        x=x+1
    else:
                   y=y+1
                   x=x+1