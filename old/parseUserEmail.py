import os
import parseSingleEmail
import sys

from collections import defaultdict




def parseUserEmails(folderName, value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent']):
    """Return parsed sections-Date, Subject, To, From,Body-  of a single user
    
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                deafult to ['sent','_sent_mail','sent_items','_sent']
    
    """
    parseUserEmails.userEmails=defaultdict(list) 
    
    
    
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
                       u=parseSingleEmail.parseSingleEmail(sent_email +"/"+email,value)
                       
                 else:
                       u=parseSingleEmail.parseSingleEmail(sent_email +"\\"+email,value)
                       
                  
                 
                 
                  
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
       
    
       
    
    


                   
