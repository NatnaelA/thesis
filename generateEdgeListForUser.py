import os

import sys
import parseUserEmail
from collections import defaultdict

def generateEgdeListForUser(folderName,value=['To', 'From'],all_sent=['sent','_sent_mail','sent_items','_sent']):
    """Generate an edgeList for a user
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                deafult to ['sent','_sent_mail','sent_items','_sent']

    
    """
   generateEgdeListForUser.edge=defaultdict(list)  
   p=parseUserEmail.parseUserEmails(folderName,value,all_sent)
   generateEgdeListForUser.edge['From']=(p['From'])
   generateEgdeListForUser.edge['To']=(p['To'])
   
    
   for i in range(0,len(generateEgdeListForUser.edge['From'])):
        for y in range(0,len(generateEgdeListForUser.edge['From'][i])):
            generateEgdeListForUser.edge['edgeList'].append(generateEgdeListForUser.edge['From'][i][y]+', '+generateEgdeListForUser.edge['To'][i][y])
      
    
   return generateEgdeListForUser.edge
