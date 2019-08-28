# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:40:28 2019

@author: Natna
"""





from collections import defaultdict

import os
from datetime import datetime
def parseSingleEmail(fileName,value=['Subject','Date','To', 'From','Body'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return parsed sections-Date, Subject, To, From,Body-for a single email
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
    start_date: the minimum date that an email can have to be considered. 
                It has a format of 'month day year'
                Default to '1 1 1998'
    
    end_date: The maximum email date that an email can have to be considered.
              It has a format of 'month day year'
              Default '31 12 2002'
    
    Returned type: a default dictionary
   
    """
    parseSingleEmail.month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    parseSingleEmail.email = defaultdict(list)
    parseSingleEmail.flag2=None
    parseSingleEmail.flag=None
    #parseEmail.email.clear()
    start_date=start_date.split()
    start_date=', '.join(start_date)
    end_date=end_date.split()
    end_date=', '.join(end_date)
    start_date=datetime.strptime(start_date,'%d, %m, %Y')
    end_date=datetime.strptime(end_date,'%d, %m, %Y')
    

            
            
    with open(fileName,'r',, encoding= 'UTF 16') as f:
             f_contents=f.readlines()
               
            
             
             blocks=f_contents[1].split()
             for thing in blocks: 
                 for i in range(1,13):
                            
                     if thing == parseSingleEmail.month[i]:
                                    
                         blocks[3]=str(i)
                         temp_date=', '.join(blocks[2:5])
                         email_date=datetime.strptime(temp_date ,'%d, %m, %Y')
                         
                         
             
             r=3
             if (email_date>=start_date and email_date<=end_date):
                
                 if('Date' in value):
                         parseSingleEmail.email['Date'].append(email_date)
                         
                         
                 if 'To' or 'From' in value:
                        
                        while(not("Subject:" in f_contents[r])):
                               
                              
                               
                                    f_contents[r].strip('\t')
                                    
                                    
                                    temp=f_contents[r].split(',')
                                    
                                    
                                    for employee in temp:
                                        employee = employee.strip()
                                        if(employee != ''):
                                       
                                           f_contents[2]=f_contents[2].strip('\n')
                                           f_contents[2]=f_contents[2].replace('From: ','')
                                           
                                           
                                           
                                           employee=employee.strip()
                                           employee=employee.replace('To: ','')
                                          
                                           
                                           if 'To' in value:
                                               parseSingleEmail.email['To'].append(employee)   
                                           
                                           
                                           
                                           
                                           if 'From' in value:
                                               parseSingleEmail.email['From'].append(f_contents[2])
                                    
                                    
                               
                                    r=r+1
                 if 'Subject' in value:
                    for line in f_contents:
                        if 'Subject:' in line:
                           # line=line.replace("Subject: ", "")
                            
                            parseSingleEmail.email['Subject'].append(line)
                            
                            
                            break
                 body=''
                 if 'Body' in value:
                    x=  f_contents.index('\n')
                    for i in  range(x,len(f_contents)):
                        body=body+ f_contents[i]
                    parseSingleEmail.email['Body'].append(body)
                   
                    
                          
    return parseSingleEmail.email
def parseAllEmails(folderName, value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return parsed sections-Date, Subject, To, From,Body-  of all the emails
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                deafult to ['sent','_sent_mail','sent_items','_sent']
    
    start_date: the minimum date that an email can have to be considered. 
                It has a format of 'month day year'
                Default to '1 1 1998'
    
    end_date: The maximum email date that an email can have to be considered.
              It has a format of 'month day year'
              Default '31 12 2002'
    
    Returned type: a default dictionary
    """
    parseAllEmails.allEmails=defaultdict(list) 
    
    file=os.listdir(folderName)
    if(type(all_sent) is not list):
        all_sent=[all_sent]
    for item in file:
        if os.name == 'posix' :  
            userEmail = parseUserEmails(folderName+'/'+item,value,all_sent,start_date,end_date)
            
        else:
            userEmail = parseUserEmails(folderName+'\\'+item,value,all_sent,start_date,end_date)
            
        if len(userEmail['Subject']) > 0:
            parseAllEmails.allEmails['Subject']=parseAllEmails.allEmails['Subject']+(userEmail['Subject'])
                      
        if len(userEmail['To'])>0 or len(userEmail['From'])>0:
            parseAllEmails.allEmails['To']=parseAllEmails.allEmails['To']+(userEmail['To'])
            
                     
        if len(userEmail['From'])>0:
            parseAllEmails.allEmails['From']=parseAllEmails.allEmails['From']+(userEmail['From'])
                      

        
        if len(userEmail['Body']) >0:
            parseAllEmails.allEmails['Body']=parseAllEmails.allEmails['Body']+(userEmail['Body'])
        if len(userEmail['Date'])>0:
            parseAllEmails.allEmails['Date']=parseAllEmails.allEmails['Date']+(userEmail['Date'])

    return parseAllEmails.allEmails
def parseUserEmails(folderName, value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return parsed sections-Date, Subject, To, From,Body-  of a single user
    
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                deafult to ['sent','_sent_mail','sent_items','_sent']
    
    start_date: the minimum date that an email can have to be considered. 
                It has a format of 'month day year'
                Default to '1 1 1998'
    
    end_date: The maximum email date that an email can have to be considered.
              It has a format of 'month day year'
              Default '31 12 2002'
    
    Returned type: a default dictionary
    
    """
    parseUserEmails.userEmails=defaultdict(list) 
    
    if(type(all_sent) is not list):
        all_sent=[all_sent]    
    
    for directory in all_sent:
        if os.name == 'posix' :    
            sent_email=folderName+'/'+directory
        else:
            sent_email=folderName+'\\'+directory
            
        if (not os.path.isdir(sent_email)): 

            #print("no "+directory +" folder for:", line)

                continue
        if (os.path.isdir(sent_email)):
            sent=os.listdir(sent_email)
            
            for email in sent:
                    #if((os.path.isfile(sent_mail +"\\"+email)):
                 if os.name == 'posix' :
                       u=parseSingleEmail(sent_email +"/"+email,value,start_date='1 1 1998',end_date='31 12 2002')
                       
                 else:
                       u=parseSingleEmail(sent_email +"\\"+email,value,start_date='1 1 1998',end_date='31 12 2002')
                       
                  
                 
                 
                  
                 if len(u['Subject']) > 0:
                      parseUserEmails.userEmails['Subject'].append(u['Subject'][0])
                      
                 if len(u['To'])>0 or len(u['From'])>0:
                      parseUserEmails.userEmails['To'].append(u['To'])
                      parseUserEmails.userEmails['From'].append(u['From'])
                     
                   
                      

        
                 if len(u['Body']) >0:
                      parseUserEmails.userEmails['Body'].append(u['Body'])
                 if len(u['Date'])>0:
                      parseUserEmails.userEmails['Date'].append(u['Date'])
                  
        
        
    return parseUserEmails.userEmails
