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
k=0
larg_pair=[]
temp=[]

t=3
file=os.listdir('.')

pairs=[]
while x < len(file):
    
    line= file[x]
    
    name=os.listdir(line)
    #  os.path.isdir(line+'/inboxadfad'
    if (os.path.isdir(line+'/_sent_mail')):
        
        sent=os.listdir(line + '/_sent_mail')
        while i<len(sent):
            pairs=[]
            if(os.path.isfile(line+'/_sent_mail'+"/"+sent[i])):
                with open(os.path.join(line+'/_sent_mail',sent[i]),'r') as f:
            
                    f_contents=f.readlines()
                   # if(f_contents[3][:2]=='To'):
                    
                    
                    r=3
                    while(not("Subject:" in f_contents[r])):
                       
                       
                       if("," in f_contents[r]):
                           
                            temp=f_contents[r].split(', ')
                            k=0
                            while(k<len(temp)):
                               #pairs=[]
                               pairs.append(f_contents[2])
                               pairs.append(temp[k])
                               larg_pair.append(pairs)
                               pairs=[]
                               k=k+1
                               
                       else:
                           
                            pairs.append(f_contents[2])
                            pairs.append(f_contents[r])
                            larg_pair.append(pairs)
                        
                       
                       
                    
                       
                       
                       
                       r=r+1
                      
            
                   # else:
                        
                    #    i=i+1
              
            r=0
            i=i+1
        i=0
        x=x+1
    else:
                   
        x=x+1
