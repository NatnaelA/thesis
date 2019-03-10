"""
Created on Mon Sep 24 16:40:52 2018

@author: Natna
"""
import os

import argparse
import sys
from datetime import datetime 
#os.chdir('C:/Users/Natna/Downloads/enron_mail_20150507.tar/maildir/')

x=0
y=0
i=0
k=0
larg_pair=[]
temp=[]
month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
t=3

pairs=[]
ap = argparse.ArgumentParser(description='directory to the email folder')
ap.add_argument('--input', help='Directroy of input files', default='C:/Users/Natna/Downloads/enron_mail_20150507.tar/maildir/', required = False)
ap.add_argument('--output', help='Directroy of output files', default='C:/Users/Natna/Documents', required = False)
ap.add_argument('--startdate', help='start date of range', default='1 1 1997', required = False)
ap.add_argument('--enddate', help='end date of range', default='31 1 2001', required = False)
args = vars(ap.parse_args())
split_start_date=args['startdate'].split()
split_end_date=args['enddate'].split()
joined_start_date=', '.join(split_start_date)
joined_end_date=', '.join(split_end_date)
start_date=datetime.strptime( joined_start_date,'%d, %m, %Y')
end_date=datetime.strptime( joined_end_date,'%d, %m, %Y')
dates=[]
#file=directory

if(not(os.path.isdir(args['input']))):
    print()
    print("Inputting data from: "+args['input'])
    print("Invalid input directory. Please specifiy correct input path to email dataset")
    print()
    ap.print_help()
    exit()
if(not(os.path.isdir(args['output']))):
    print()
    print("Outputting result to directory: "+args['output'])
    print("Invalid output directory. Please specifiy correct output path for result set")
    print()
    ap.print_help()
    exit()
file=os.listdir(args['input'])

from collections import defaultdict
sendDict = defaultdict(set)

numFiles = 0
numProcessed = 0

for line in file:
    numFiles += 1 
    print("checking folder #", numFiles, ': ', line, sep = '')

    sent_mail = args['input']+'/'+line+'/_sent_mail'
    
    if (not os.path.isdir(sent_mail)): 
        print("no sent mail for:", line)
        

    if (os.path.isdir(sent_mail)):
        numProcessed += 1
        sent=os.listdir(sent_mail)
        for email in sent:
            pairs=[]
            if(os.path.isfile(sent_mail +"/"+email)):
                with open(os.path.join(sent_mail,email),'r') as f:
            
                    f_contents=f.readlines()
                    
                        
                    blocks=f_contents[1].split()
                    for thing in blocks:
                        for i in range(1,13):
                        
                            if thing == month[i]:
                                
                                blocks[3]=str(i)
                                temp_date=', '.join(blocks[2:5])
                                email_date=datetime.strptime(temp_date ,'%d, %m, %Y')
                                
                                
                                break 
                        
                if(start_date<=email_date and email_date<=end_date ):
                        
                  
                    
                    r=3
                    while(not("Subject:" in f_contents[r])):
                       
                      
                       
                            f_contents[r].strip('\t')
                            
                            
                            temp=f_contents[r].split(',')
                            
                            k=0
                            for employee in temp:
                                employee = employee.strip()
                                if(employee != ''):
                               
                                   f_contents[2]=f_contents[2].strip('\n')
                                   f_contents[2]=f_contents[2].replace('From: ','')
                                   pairs.append(f_contents[2])
                                   sendDict[line].add(f_contents[2])

                                   employee=employee.strip()
                                   employee=employee.replace('To: ','')
                                   pairs.append(employee)
                                   pairs.append(email)
                                   larg_pair.append(pairs)
                                   
                                   pairs=[]
                                   
                       
                       
                            r=r+1
                      
            
print()
print("Number of folders searched: ", numFiles)
print("Number of folders processed: ", numProcessed)
print("Number of folders skipped: ", numFiles - numProcessed)
print()

print("outputting edge list to:", args['output'] + '/edgelist.csv')
with open(args['output']+'/'+'edgelist.csv','w+') as list:
   for item in larg_pair:
       edge_list=', '.join(item)
       list.write(edge_list+'\n')

for senders in sendDict :
    print(senders, ":" , sendDict[senders])

