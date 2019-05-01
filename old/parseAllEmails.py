import os
import parseUserEmail
import sys

from collections import defaultdict

def parseAllEmails(folderName, value=['Subject','Date','To', 'From','Body']):
    """Return parsed sections-Date, Subject, To, From,Body-  of all the emails
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                deafult to ['sent','_sent_mail','sent_items','_sent']
    """
    parseAllEmails.allEmails=defaultdict(list) 
    
    file=os.listdir(folderName)
    for item in file:
        if os.name == 'posix' :  
            userEmail = parseUserEmail.parseUserEmails(folderName+'/'+item,value)
            
        else:
            userEmail = parseUserEmail.parseUserEmails(folderName+'\\'+item,value)
            
        if len(userEmail['Subject']) > 0:
            parseAllEmails.allEmails['Subject']=parseAllEmails.allEmails['Subject']+(userEmail['Subject'])
                      
        if len(userEmail['To'])>0 or len(userEmail['From'])>0:
            parseAllEmails.allEmails['To']=parseAllEmails.allEmails['To']+(userEmail['To'])
            parseAllEmails.allEmails['From']=parseAllEmails.allEmails['From']+(userEmail['From'])
                     
                   
                      

        
        if len(userEmail['Body']) >0:
            parseAllEmails.allEmails['Body']=parseAllEmails.allEmails['Body']+(userEmail['Body'])
        if len(userEmail['Date'])>0:
            parseAllEmails.allEmails['Date']=parseAllEmails.allEmails['Date']+(userEmail['Date'])

    return parseAllEmails.allEmails

   
