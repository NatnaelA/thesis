"""
Created on Mon Sep 24 16:40:52 2018

@author: Natna
"""
import os
import parse_Email
import argparse
import sys
from datetime import datetime 
#os.chdir('C:/Users/Natna/Downloads/enron_mail_20150507.tar/maildir/')



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
all_sent=[]
all_sent=['/sent','/_sent_mail','/sent_items']
for line in file:
    numFiles += 1 
    print("checking folder #", numFiles, ': ', line)
    for directory in all_sent:
        sent_mail = args['input']+'/'+line+directory
        
        if (not os.path.isdir(sent_mail)): 
            print("no "+directory +" folder for:", line)
            continue
    
        if (os.path.isdir(sent_mail)):
            numProcessed += 1
            sent=os.listdir(sent_mail)
            for email in sent:
                pairs=[]
                if(os.path.isfile(sent_mail +"/"+email)):
                   parse_Email(sent_mail +"/"+email,['To','From','subject','body',{'start_date':start_date,'end_date':end_date}])
                            
        
                             
                   
                            
                      
            
print()
print("Number of folders searched: ", numFiles)
print("Number of folders processed: ", numProcessed)
print("Number of folders skipped: ", numFiles - numProcessed)
print()

print("outputting edge list to:", args['output'] + '/edgelist.csv')
with open(args['output']+'/'+'edgelist.csv','w+') as list:
   for item in parse_Email.large_pair:
       edge_list=', '.join(item)
       list.write(edge_list+'\n')
print('This is the subject'+parse_Email.subject)
print('This is the body'+parse_Email.body)
for senders in sendDict :
    print(senders, ":" , sendDict[senders])

