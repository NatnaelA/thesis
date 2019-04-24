import os

import sys
import parseUserEmail
from textblob import TextBlob


def sentAnalysis(folderName,value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent']):
    """Return a list of sentiment analysis for a user
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
           
           
    all_sent:contains the directory to all the sent emails
                can be user specified
                deafult to ['sent','_sent_mail','sent_items','_sent']
    """
    sentAnalysis.scores=[]
    test=[]
    
    p=parseUserEmail.parseUserEmails(folderName,value,all_sent)
    if 'Subject' in value and 'Body' in value and 'Date' not in value:
        
        for item in p['Subject']:
            blob_for_subject=TextBlob(item)
           
            sentAnalysis.scores.append(blob_for_subject.sentiment.polarity)
        for i in range(0,len(p['Body'])):
            
                blob_for_body=TextBlob(p['Body'][i][0])
                sentAnalysis.scores.append(blob_for_body.sentiment.polarity)
    elif 'Subject' in value and 'Body' in value and 'Date' in value:
        
        for i in range(0,len(p['Subject'])):
            blob_for_subject=TextBlob(p['Subject'][i])
            
            
            test.append(blob_for_subject.sentiment.polarity)
            test.append(p['Date'][i])
            sentAnalysis.scores.append(test)
            test=[]
        for i in range(0,len(p['Body'])):
            
                blob_for_body=TextBlob(p['Body'][i][0])
                
                test.append(blob_for_body.sentiment.polarity)
                test.append(p['Date'][i])
                sentAnalysis.scores.append(test)
                test=[]
    elif 'Body' in value and 'Subject' not in value and 'Date' not in value:
        
        for i in range(0,len(p['Body'])):
            
                
                blob_for_body=TextBlob(p['Body'][i][0])
                sentAnalysis.scores.append(blob_for_body.sentiment.polarity)
    elif 'Body' in value and 'Subject' not in value and 'Date' in value:
            
            for i in range(0,len(p['Body'])):
                
                    blob_for_body=TextBlob(p['Body'][i][0])
                    
                    test.append(blob_for_body.sentiment.polarity)
                    test.append(p['Date'][i])
                    sentAnalysis.scores.append(test)
                    test=[]
    elif 'Body' not in value and 'Subject' in value and 'Date' not in value:
        for item in p['Subject']:
            
            blob_for_subject=TextBlob(item)
            sentAnalysis.scores.append(blob_for_subject.sentiment.polarity)
    elif 'Body' not in value and 'Subject' in value and 'Date' in value:
        for i in range(0,len(p['Subject'])):
            blob_for_subject=TextBlob(p['Subject'][i])
            test.append(blob_for_subject.sentiment.polarity)
            test.append(p['Date'][i])
            sentAnalysis.scores.append(test)
            test=[]
    
    return sentAnalysis.scores          
  
