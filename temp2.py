# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 16:40:52 2018

@author: Natna
"""
import os
import networkx as nx
from networkx.algorithms import community 
import argparse
import sys
#os.chdir('C:/Users/Natna/Downloads/enron_mail_20150507.tar/maildir/')
G=nx.path_graph(10)
co=community.k_clique_communities
x=0
y=0
i=0
k=0
larg_pair=[]
temp=[]

t=3

pairs=[]
ap = argparse.ArgumentParser(description='directory to the email folder')
ap.add_argument('input directory',help='Directroy of input files', default='C:/Users/Natna/Downloads/enron_mail_20150507.tar/maildir/')

args = vars(ap.parse_args())
file=os.listdir(args['input directory'])
#file=directory
while x < len(file):
    
    line= file[x]
    
    
    #  os.path.isdir(line+'/inboxadfad'
    if (os.path.isdir(args['input directory']+'/'+line+'/_sent_mail')):
        
        sent=os.listdir(args['input directory']+'/'+line + '/_sent_mail')
        while i<len(sent):
            pairs=[]
            if(os.path.isfile(args['input directory']+'/'+line+'/_sent_mail'+"/"+sent[i])):
                with open(os.path.join(args['input directory']+'/'+line+'/_sent_mail',sent[i]),'r') as f:
            
                    f_contents=f.readlines()
                   
        
                        
                        
                       
                        
                   # if(f_contents[3][:2]=='To'):
                    
                    
                    r=3
                    while(not("Subject:" in f_contents[r])):
                       
                      
                       if("," in f_contents[r]):
                            f_contents[r].strip('\t')
                            
                            temp=f_contents[r].split(',')
                            
                            k=0
                            while(k<len(temp)):
                                if(temp[k] != ''):
                               #pairs=[]
                                   f_contents[2]=f_contents[2].strip()
                                   f_contents[2]=f_contents[2].strip('From: ')
                                   pairs.append(f_contents[2])
                                   temp[k]=temp[k].strip()
                                   temp[k]=temp[k].strip('To: ')
                                   pairs.append(temp[k])
                                   pairs.append(sent[i])
                                   larg_pair.append(pairs)
                                   
                                   pairs=[]
                                   k=k+1
                                else:
                                    print(temp[k])
                                    k=k+1
                                     
                               
                       else:
                               if(f_contents[r] != ''):
                                    f_contents[2]=f_contents[2].strip()
                                    f_contents[2]=f_contents[2].strip('From: ')
                                    pairs.append(f_contents[2])
                                    
                                    f_contents[r]=f_contents[r].strip()
                                    f_contents[r]=f_contents[r].strip('To: ')
                                    pairs.append(f_contents[r])
                                    pairs.append(sent[i])
                                    larg_pair.append(pairs)
                               else:
                                    r=r+1
                                
                                
                                
                       
                       
                    
                       
                       
                       
                       r=r+1
                      
            
                   # else:
                        
                    #    i=i+1
              
           
            i=i+1
        i=0
        x=x+1
    else:
                   
        x=x+1
