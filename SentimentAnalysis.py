# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:45:22 2019

@author: belayn
"""
import os

import sys
import numpy as np
import parseEmail
from textblob import TextBlob
from collections import defaultdict
import matplotlib as plt
import matplotlib.pyplot as plt
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber

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
    i=0
    if(type(all_sent) is not list):
        all_sent=[all_sent]    
    for item in file:
        if os.name == 'posix' :
           
            sentForUser = userSentAnalysis(folderName+'/'+item,value,all_sent,start_date,end_date)
            
            allsentimentAnalysis.scores['Body'].append(sentForUser['Body'])
            allsentimentAnalysis.scores['Subject'].append(sentForUser['Subject'])
            print(userSentAnalysis(folderName+'/'+item,value,all_sent,start_date,end_date))
        else:
            print("Checking for user"+item)
            print(i+1)
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
   
    p=parseEmail.parseUserEmails(folderName,value,all_sent,start_date,end_date)
    if 'Subject' in value and 'Body' in value and 'Date' not in value:
        print("it is here",1)
        for item in p['Subject']:
            blob_for_subject=TextBlob(item)
           
            userSentAnalysis.scores['Subject'].append(blob_for_subject.sentiment.polarity)
        for i in range(0,len(p['Body'])):
            
                blob_for_body=TextBlob(p['Body'][i][0])
                userSentAnalysis.scores['Body'].append(blob_for_body.sentiment.polarity)
    elif 'Subject' in value and 'Body' in value and 'Date' in value:
        print("it is here",2)
        
        p['Subject']=set(p['Subject'])
        p['Subject']=list(p['Subject'])
        
        #for i in range(0,len(p['Subject'])):
            #blob_for_subject=TextBlob(p['Subject'][i])
            
            
           # test.append(blob_for_subject.sentiment.polarity)
            #test.append(blob_for_subject.sentiment.subjectivity)
            #test.append(p['Date'][i][0])
            #userSentAnalysis.scores['Subject'].append(test)
            #test=[]
        for i in range(0,len(p['Body'])):
            
                blob_for_body=TextBlob(p['Body'][i][0])
                #tb=Blobber(analyzer=NaiveBayesAnalyzer())
                #blob_for_body_with_naive= tb(p['Body'][i][0])
                
                test.append(blob_for_body.sentiment.polarity)
                #test.append(blob_for_body_with_naive.sentiment.p_pos)
                test.append(p['Date'][i][0])
                #test.append(blob_for_body.sentiment.subjectivity)
                #test.append(len(p['Body'][i][0].split()))
                userSentAnalysis.scores['Body'].append(test)
                
                test=[]
    elif 'Body' in value and 'Subject' not in value and 'Date' not in value:
        print("it is here",3)
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
        print("it is here",4)
        for item in p['Subject']:
            
            blob_for_subject=TextBlob(item)
            userSentAnalysis.scores['Subject'].append(blob_for_subject.sentiment.polarity)
    elif 'Body' not in value and 'Subject' in value and 'Date' in value:
        print("it is here",5)
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
            
            val=folderName.split('\\')[4]
            values = set(map(lambda x:(x[1].year,x[1].month), graphForUser.userSentScores['Body']))
            if graphType=='line':
                newlist = [[(y[0],y[1]) for y in graphForUser.userSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
               
                drawLineGraph(values,newlist,val)
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForUser.userSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                drawBoxPlot(boxlist)
            
            values = set(map(lambda x:(x[1].year,x[1].month), graphForUser.userSentScores['Subject']))
            if graphType=='line':
                newlist = [[(y[0],y[1]) for y in graphForUser.userSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForUser.userSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
           
    if graphType =='line':
       
        
        drawLineGraph(values,newlist,val)
    elif graphType=='boxplot':
        drawBoxPlot(boxlist)
def graphForAll(folderName,value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002', graphType='line'):
    graphForAll.allSentScores=allsentimentAnalysis(folderName, value, all_sent, start_date, end_date)
   
    values=[]
    graphForAll.newlist=[]
    boxlist=[]
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
            print(values)
            if graphType=='line':
                graphForAll.newlist = [[(y[0]) for y in graphForAll.allSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
                drawLineGraph(values, graphForAll.newlist)
            elif graphType=='boxplot':
                boxlist = [[y[0] for y in graphForAll.allSentScores['Body'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                print(graphForAll.allSentScores['Body'])
                drawBoxPlot(boxlist)
            
                #values = set(map(lambda x:(x[1].year,x[1].month), graphForAll.allSentScores['Subject']))
            #if graphType=='line':
                #newlist = [[(y[0],y[1]) for y in graphForAll.allSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
            #elif graphType=='boxplot':
                #boxlist = [[y[0] for y in graphForAll.allSentScores['Subject'] if (y[1].month==x[1] and y[1].year==x[0] )] for x in values]
                
    if graphType =='line':
        drawLineGraph(values, graphForAll.newlist)
    elif graphType=='boxplot':
       drawBoxPlot(boxlist)
    #item=os.listdir(folderName)
#    graphForAll.n=0
    


#def drawLineGraph(values,newlist,user):
def drawLineGraph(values,newlist):
    
    
#    l=[]

    
#    years=[(1998,10),(1998,11),(1998,12),(1999,1),(1999,2),(1999,3),(1999,4),(1999,5),
#                             (1999,6),(1999,7),(1999,8),(1999,9),(1999,10),(1999,11),(1999,12),(2000,1),(2000,2),(2000,3),
#                             (2000,4),(2000,5),(2000,6)
#                             ,(2000,7),(2000,8),(2000,9),(2000,10),(2000,11),(2000,12),(2001,1),(2001,2),(2001,3),(2001,4)
#                             ,(2001,5),(2001,6),(2001,7),(2001,8),(2001,9),(2001,10)
#                             ,(2001,11),(2001,12),(2002,1),(2002,2),(2002,3),(2002,4),(2002,5),(2002,6)
#                             ,(2002,7)]
   
        
    drawLineGraph.flag=False
    y=[]
    x=[]
    
    l=set()
#    for th in years:
#        
#        l.append([th,0])
    
    for i in newlist:
        val=0
        for c in i:
    
            val=val+c[0]
            
#        p=l.index([(c[1].year, c[1].month),0])
#        l[p][1]=val/len(i)
        l.add(((c[1].year, c[1].month),val/len(i)))
           #l.add(((c[1].year, c[1].month),len(i)))
           #break
    

    l=sorted(list(l))
#    graphForAll.n.append(l)
    for v in l:
       y.append(v[1])
       x.append(str(v[0]))
    
    
#    if drawLineGraph.flag==True:
    num=0
    #palette = plt.get_cmap('Set1')
    for i in l:
            
          
        num+=1
        plt.plot(x,y,marker='', linewidth=1, alpha=0.9)
        plt.xticks(rotation=90)
    

    
    plt.xlabel("Years")
    plt.ylabel("Sentiment")
    
    
def drawBoxPlot(boxlist):
   
    plt.boxplot(boxlist)
    