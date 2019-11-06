# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:45:22 2019

@author: belayn
"""
import os

import sys

import parseEmail
from textblob import TextBlob
from collections import defaultdict
import matplotlib as plt
import matplotlib.pyplot as plt

def allsentimentAnalysis(folderName,value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
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
    allsentimentAnalysis.scores=defaultdict(list)
    body=[]
    subject=[]
    if(type(all_sent) is not list):
        all_sent=[all_sent]    
    for item in file:
        if os.name == 'posix' :
           
            sentForUser = userSentAnalysis(folderName+'/'+item,value,all_sent,start_date,end_date)
            allsentimentAnalysis.scores['Body'].append(sentForUser['Body'])
            allsentimentAnalysis.scores['Subject'].append(sentForUser['Subject'])
            print(userSentAnalysis(folderName+'/'+item,value,all_sent,start_date,end_date))
        else:
           
            sentForUser = userSentAnalysis(folderName+'\\'+item,value,all_sent,start_date,end_date)
            body.append(sentForUser['Body'])
            subject.append(sentForUser['Subject'])
            
        #allsentimentAnalysis.scores=allsentimentAnalysis.scores+sentForUser
    
    allsentimentAnalysis.scores['Body']= body [0]
    for i in range ( 1, len(body)):
        allsentimentAnalysis.scores['Body']=allsentimentAnalysis.scores['Body']+body[i]
    for i in range ( 1, len(subject)):
        allsentimentAnalysis.scores['Subject']=allsentimentAnalysis.scores['Subject']+subject[i]
        
        
    return  allsentimentAnalysis.scores
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
    userSentAnalysis.scores=defaultdict(list)
    test=[]

    if(type(all_sent) is not list):
        all_sent=[all_sent]
   
    p=parseEmail.parseUserEmails(folderName,value,all_sent)
    if 'Subject' in value and 'Body' in value and 'Date' not in value:
        
        for item in p['Subject']:
            blob_for_subject=TextBlob(item)
           
            userSentAnalysis.scores['Subject'].append(blob_for_subject.sentiment.polarity)
        for i in range(0,len(p['Body'])):
            
                blob_for_body=TextBlob(p['Body'][i][0])
                userSentAnalysis.scores['Body'].append(blob_for_body.sentiment.polarity)
    elif 'Subject' in value and 'Body' in value and 'Date' in value:
        p['Subject']=set(p['Subject'])
        p['Subject']=list(p['Subject'])
        
        for i in range(0,len(p['Subject'])):
            blob_for_subject=TextBlob(p['Subject'][i])
            
            
            test.append(blob_for_subject.sentiment.polarity)
            test.append(p['Date'][i][0])
            userSentAnalysis.scores['Subject'].append(test)
            test=[]
        for i in range(0,len(p['Body'])):
            
                blob_for_body=TextBlob(p['Body'][i][0])
                
                test.append(blob_for_body.sentiment.polarity)
               
                test.append(p['Date'][i][0])
                userSentAnalysis.scores['Body'].append(test)
                test=[]
    elif 'Body' in value and 'Subject' not in value and 'Date' not in value:
        
        for i in range(0,len(p['Body'])):
            
                
                blob_for_body=TextBlob(p['Body'][i][0])
                userSentAnalysis.scores['Body'].append(blob_for_body.sentiment.polarity)
    elif 'Body' in value and 'Subject' not in value and 'Date' in value:
            
            for i in range(0,len(p['Body'])):
                
                    blob_for_body=TextBlob(p['Body'][i][0])
                    
                    test.append(blob_for_body.sentiment.polarity)
                    test.append(p['Date'][i][0])
                    userSentAnalysis.scores['Body'].append(test)
                    test=[]
    elif 'Body' not in value and 'Subject' in value and 'Date' not in value:
        
        for item in p['Subject']:
            
            blob_for_subject=TextBlob(item)
            userSentAnalysis.scores['Subject'].append(blob_for_subject.sentiment.polarity)
    elif 'Body' not in value and 'Subject' in value and 'Date' in value:
        
        for i in range(0,len(p['Subject'])):
            blob_for_subject=TextBlob(p['Subject'][i])
            test.append(blob_for_subject.sentiment.polarity)
            test.append(p['Date'][i][0])
            userSentAnalysis.scores['Subject'].append(test)
            test=[]
            

    
    
    return userSentAnalysis.scores          
def graphForUser(folderName,value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002', graphType='line'):
    graphForUser.userSentScores=userSentAnalysis(folderName, value, all_sent, start_date, end_date)
    values=[]
    newlist=[]
    if ('Subject' not in value and 'Body' in value):
        values = set(map(lambda x:(x[1].year,x[1].month), graphForUser.userSentScores['Body']))
        if graphType=='line':
            newlist = [[(y[0],y[1]) for y in graphForUser.userSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
        elif graphType=='boxplot':
            boxlist = [[y[0] for y in graphForUser.userSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
    elif ('Subject'  in value and 'Body' not in value):
            values = set(map(lambda x:(x[1].year,x[1].month), graphForUser.userSentScores['Subject']))
            if graphType=='line':
                newlist = [[(y[0],y[1]) for y in graphForUser.userSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForUser.userSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
            
    elif ('Subject'  in value and 'Body' in value):
            

            values = set(map(lambda x:(x[1].year,x[1].month), graphForUser.userSentScores['Body']))
            if graphType=='line':
                newlist = [[(y[0],y[1]) for y in graphForUser.userSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                drawLineGraph(values,newlist)
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForUser.userSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                drawBoxPlot(boxlist)
            
            values = set(map(lambda x:(x[1].year,x[1].month), graphForUser.userSentScores['Subject']))
            if graphType=='line':
                newlist = [[(y[0],y[1]) for y in graphForUser.userSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForUser.userSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
    if graphType =='line':
        drawLineGraph(values,newlist)
    elif graphType=='boxplot':
        drawBoxPlot(boxlist)
def graphForAll(folderName,value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002', graphType='line'):
    graphForAll.allSentScores=allsentimentAnalysis(folderName, value, all_sent, start_date, end_date)
    values=None
    newlist=None
    boxlist=None
    if ('Subject' not in value and 'Body' in value):
        values = set(map(lambda x:(x[1].year,x[1].month), graphForAll.allSentScores['Body']))
        if graphType=='line':
            newlist = [[(y[0],y[1]) for y in graphForAll.allSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
        elif graphType=='boxplot':
            boxlist = [[y[0] for y in graphForAll.allSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
    elif ('Subject'  in value and 'Body' not in value):
            values = set(map(lambda x:(x[1].year,x[1].month), graphForAll.allSentScores['Subject']))
            if graphType=='line':
                newlist = [[(y[0],y[1]) for y in graphForAll.allSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForAll.allSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
    elif ('Subject'  in value and 'Body' in value):
            values = set(map(lambda x:(x[1].year,x[1].month), graphForAll.allSentScores['Body']))
            if graphType=='line':
                newlist = [[(y[0],y[1]) for y in graphForAll.allSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                drawLineGraph(values,newlist)
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForAll.allSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                drawBoxPlot(boxlist)
            
            values = set(map(lambda x:(x[1].year,x[1].month), graphForAll.allSentScores['Subject']))
            if graphType=='line':
                newlist = [[(y[0],y[1]) for y in graphForAll.allSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForAll.allSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
    if graphType =='line':
        drawLineGraph(values,newlist)
    elif graphType=='boxplot':
        drawBoxPlot(boxlist)
def drawLineGraph(values, newlist):

    l=set()
    y=[]
    x=[]
    for i in newlist:
        val=0
        for c in i:
    
            val=val+c[0]
        l.add(((c[1].year, c[1].month),val/len(i)))
    

    l=sorted(list(l))
    for v in l:
       y.append(v[1])
       x.append(str(v[0]))
    
    
    for i in l:
        plt.plot(x,y)
        plt.xticks(rotation=90)

def drawBoxPlot(boxlist):
    plt.boxplot(boxlist)
    
