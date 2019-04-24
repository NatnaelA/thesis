# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:45:22 2019

@author: belayn
"""
import os

import sys
import UserSentimentAnalysis

def allsentimentAnalysis(folderName,value=['To', 'From'],all_sent=['sent','_sent_mail','sent_items','_sent']):
    """Return a list of sentiment analysis for all the emails
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                deafult to ['sent','_sent_mail','sent_items','_sent']
    
    """
    file=os.listdir(folderName)
    allsentimentAnalysis.scores=[]
    
    for item in file:
        if os.name == 'posix' :  
            sentForUser = UserSentimentAnalysis.sentAnalysis(folderName+'/'+item,value,all_sent)
            
        else:
            
            sentForUser = UserSentimentAnalysis.sentAnalysis(folderName+'\\'+item,value,all_sent)
        
        allsentimentAnalysis.scores=allsentimentAnalysis.scores+sentForUser
    
    
    return allsentimentAnalysis.scores