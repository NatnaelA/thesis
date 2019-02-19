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
ap.add_argument('--input', help='Directroy of input files', default='C:/Users/Natna/Downloads/enron_mail_20150507.tar/maildir/', required = False)
ap.add_argument('--output', help='Directroy of output files', default='C:/Users/Natna/Documents', required = False)
ap.add_argument('--startdate', help='start date of range', default='01 Jan 1999', required = False)
ap.add_argument('--enddate', help='end date of range', default='12 31 2001', required = False)
args = vars(ap.parse_args())

file=os.listdir(args['input'])
#file=directory
for line in file:
    
    
    
    
    #  os.path.isdir(line+'/inboxadfad'
    if (os.path.isdir(args['input']+'/'+line+'/_sent_mail')):
        
        sent=os.listdir(args['input']+'/'+line + '/_sent_mail')
        for email in sent:
            pairs=[]
            if(os.path.isfile(args['input']+'/'+line+'/_sent_mail'+"/"+email)):
                with open(os.path.join(args['input']+'/'+line+'/_sent_mail',email),'r') as f:
            
                    f_contents=f.readlines()
                   
        
                        
        
                        
                   # if(f_contents[3][:2]=='To'):
                #range for dates
                    
                    r=3
                    while(not("Subject:" in f_contents[r])):
                       
                      
                       if("," in f_contents[r]):
                            f_contents[r].strip('\t')
                            
                            temp=f_contents[r].split(',')
                            
                            k=0
                            for employee in temp:
                                employee = employee.strip()
                                if(employee != ''):
                               #pairs=[]
                                   f_contents[2].strip()
                                   f_contents[2]=f_contents[2].strip('From: ')
                                   pairs.append(f_contents[2])
                                   employee=employee.strip()
                                   employee=employee.strip('To: ')
                                   pairs.append(employee)
                                   pairs.append(email)
                                   larg_pair.append(pairs)
                                   
                                   pairs=[]
                                   
                                     
                               
                       else:
                               if(f_contents[r] != ''):
                                    f_contents[2].strip()
                                    f_contents[2]=f_contents[2].strip('From: ')
                                    pairs.append(f_contents[2])
                                    
                                    f_contents[r]=f_contents[r].strip()
                                    f_contents[r]=f_contents[r].strip('To: ')
                                    pairs.append(f_contents[r])
                                    pairs.append(email)
                                    larg_pair.append(pairs)
                               else:
                                    r=r+1
                                
                                
                                
                       
                       
                    
                       
                       
                       
                       r=r+1
                      
            
                   # else:
                        
                    #    i=i+1
        


# print edge list
with open(args['output']+'/'+'edgelist.csv','w+') as list:
    for item in larg_pair:
        list.write(str(item)+'\n')

