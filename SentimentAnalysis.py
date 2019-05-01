# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:45:22 2019

@author: belayn
"""
import os

import sys

import parseEmail
from textblob import TextBlob

def allsentimentAnalysis(folderName,value=['To', 'From'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return a list of sentiment analysis for all the emails
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                default to ['sent','_sent_mail','sent_items','_sent']
                
    start_date: the minimum date that an email can have to be considered. 
                It has a format of 'month day year'
                Default to '1 1 1998'
    
    end_date: The maximum email date that an email can have to be considered.
              It has a format of 'month day year'
              Default '31 12 2002'
              
    
    Returned type: a list
    
    """
    file=os.listdir(folderName)
    allsentimentAnalysis.scores=[]
    if(type(all_sent) is not list):
        all_sent=[all_sent]    
    for item in file:
        if os.name == 'posix' :  
            sentForUser = userSentAnalysis(folderName+'/'+item,value,all_sent,start_date,end_date)
            
        else:
            
            sentForUser = userSentAnalysis(folderName+'\\'+item,value,all_sent,start_date,end_date)
        
        allsentimentAnalysis.scores=allsentimentAnalysis.scores+sentForUser
    
    
    return allsentimentAnalysis.scores
def userSentAnalysis(folderName,value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return a list of sentiment analysis for a user
    
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
    Returned type: a list
    """
    userSentAnalysis.scores=[]
    test=[]
    if(type(all_sent) is not list):
        all_sent=[all_sent]    
    p=parseEmail.parseUserEmails(folderName,value,all_sent)
    if 'Subject' in value and 'Body' in value and 'Date' not in value:
        
        for item in p['Subject']:
            blob_for_subject=TextBlob(item)
           
            userSentAnalysis.scores.append(blob_for_subject.sentiment.polarity)
        for i in range(0,len(p['Body'])):
            
                blob_for_body=TextBlob(p['Body'][i][0])
                userSentAnalysis.scores.append(blob_for_body.sentiment.polarity)
    elif 'Subject' in value and 'Body' in value and 'Date' in value:
        
        for i in range(0,len(p['Subject'])):
            blob_for_subject=TextBlob(p['Subject'][i])
            
            
            test.append(blob_for_subject.sentiment.polarity)
            test.append(p['Date'][i])
            userSentAnalysis.scores.append(test)
            test=[]
        for i in range(0,len(p['Body'])):
            
                blob_for_body=TextBlob(p['Body'][i][0])
                
                test.append(blob_for_body.sentiment.polarity)
                test.append(p['Date'][i])
                userSentAnalysis.scores.append(test)
                test=[]
    elif 'Body' in value and 'Subject' not in value and 'Date' not in value:
        
        for i in range(0,len(p['Body'])):
            
                
                blob_for_body=TextBlob(p['Body'][i][0])
                userSentAnalysis.scores.append(blob_for_body.sentiment.polarity)
    elif 'Body' in value and 'Subject' not in value and 'Date' in value:
            
            for i in range(0,len(p['Body'])):
                
                    blob_for_body=TextBlob(p['Body'][i][0])
                    
                    test.append(blob_for_body.sentiment.polarity)
                    test.append(p['Date'][i])
                    userSentAnalysis.scores.append(test)
                    test=[]
    elif 'Body' not in value and 'Subject' in value and 'Date' not in value:
        for item in p['Subject']:
            
            blob_for_subject=TextBlob(item)
            userSentAnalysis.scores.append(blob_for_subject.sentiment.polarity)
    elif 'Body' not in value and 'Subject' in value and 'Date' in value:
        for i in range(0,len(p['Subject'])):
            blob_for_subject=TextBlob(p['Subject'][i])
            test.append(blob_for_subject.sentiment.polarity)
            test.append(p['Date'][i])
            userSentAnalysis.scores.append(test)
            test=[]
    
    return userSentAnalysis.scores          
  