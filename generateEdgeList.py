import os

import sys

import parseEmail
from collections import defaultdict

def generateAllEgdeList(folderName,value=['To', 'From'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return an edgeList for all the emails
    
    
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
    file=os.listdir(folderName)
    generateAllEgdeList.edge=defaultdict(list)  
    if(type(all_sent) is not list):
        all_sent=[all_sent]
    
    for item in file:
        if os.name == 'posix' :  
            egdeForUser = generateEgdeListForUser(folderName+'/'+item,value,all_sent,start_date,end_date)
            
        else:
            
            egdeForUser = generateEgdeListForUser(folderName+'\\'+item,value,all_sent,start_date,end_date)
        
        generateAllEgdeList.edge['egdeList']=generateAllEgdeList.edge['egdeList']+egdeForUser['edgeList']
    
    
    return generateAllEgdeList.edge

def generateEgdeListForUser(folderName,value=['To', 'From'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
   """Generate an edgeList for a user
    
    
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
   if(type(all_sent) is not list):
        all_sent=[all_sent]
   
    
   generateEgdeListForUser.edge=defaultdict(list)  
   p=parseEmail.parseUserEmails(folderName,value,all_sent,start_date,end_date)
   generateEgdeListForUser.edge['From']=(p['From'])
   generateEgdeListForUser.edge['To']=(p['To'])
   
    
   for i in range(0,len(generateEgdeListForUser.edge['From'])):
        for y in range(0,len(generateEgdeListForUser.edge['From'][i])):
            generateEgdeListForUser.edge['edgeList'].append(generateEgdeListForUser.edge['From'][i][y]+', '+generateEgdeListForUser.edge['To'][i][y])
      
    
   return generateEgdeListForUser.edge
