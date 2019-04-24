import os

import sys
import generateEdgeListForUser
from collections import defaultdict

def generateAllEgdeList(folderName,value=['To', 'From'],all_sent=['sent','_sent_mail','sent_items','_sent']):
    """Return an edgeList for all the emails
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                deafult to ['sent','_sent_mail','sent_items','_sent']
    
    """
    file=os.listdir(folderName)
    generateAllEgdeList.edge=defaultdict(list)  
    
    for item in file:
        if os.name == 'posix' :  
            egdeForUser = generateEdgeListForUser.generateEgdeListForUser(folderName+'/'+item,value,all_sent)
            
        else:
            
            egdeForUser = generateEdgeListForUser.generateEgdeListForUser(folderName+'\\'+item,value,all_sent)
        
        generateAllEgdeList.edge['egdeList']=generateAllEgdeList.edge['egdeList']+egdeForUser['edgeList']
    
    
    return generateAllEgdeList.edge