# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:40:28 2019

@author: Natna
"""





from collections import defaultdict

import os
from datetime import datetime
def parseSingleEmail(fileName,value=['Subject','Date','To', 'From','Body'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return parsed sections-Date, Subject, To, From,Body-for a single email
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
    start_date: the minimum date that an email can have to be considered. 
                It has a format of 'month day year'
                Default to '1 1 1998'
    
    end_date: The maximum email date that an email can have to be considered.
              It has a format of 'month day year'
              Default '31 12 2002'
    
    Returned type: a default dictionary
   
    """
    parseSingleEmail.month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    parseSingleEmail.email = defaultdict(list)
    parseSingleEmail.flag2=None
    parseSingleEmail.flag=None
    #parseEmail.email.clear()
    start_date=start_date.split()
    start_date=', '.join(start_date)
    end_date=end_date.split()
    end_date=', '.join(end_date)
    start_date=datetime.strptime(start_date,'%d, %m, %Y')
    end_date=datetime.strptime(end_date,'%d, %m, %Y')
    emails=[
 'albert.meyers@enron.com',
 'andrea.ring@enron.com',
 'andrew.lewis@enron.com',
 'andy.zipper@enron.com',
 'b..sanders@enron.com',
 'barry.tycholiz@enron.com',
 'benjamin.rogers@enron.com',
 'bill.rapp@enron.com',
 'bill.williams@enron.com',
 'brad.mckay@enron.com',
 'c..giron@enron.com',
 'cara.semperger@enron.com',
 'carol.clair@enron.com',
 'chris.dorland@enron.com',
 'chris.germany@enron.com',
 'clint.dean@enron.com',
 'cooper.richey@enron.com',
 'd..steffes@enron.com',
 'd..thomas@enron.com',
 'dan.hyvl@enron.com',
 'dana.davis@enron.com',
 'danny.mccarty@enron.com',
 'daren.farmer@enron.com',
 'darrell.schoolcraft@enron.com',
 'david.delainey@enron.com',
 'debra.perlingiere@enron.com',
 'diana.scholtes@enron.com',
 'don.baughman@enron.com',
 'doug.gilbert-smith@enron.com',
 'drew.fossum@enron.com',
 'dutch.quigley@enron.com',
 'e..haedicke@enron.com',
 'elizabeth.sager@enron.com',
 'eric.bass@enron.com',
 'eric.linder@enron.com',
 'eric.saibi@enron.com',
 'errol.mclaughlin@enron.com',
 'f..brawner@enron.com',
 'frank.ermis@enron.com',
 'geir.solberg@enron.com',
 'geoff.storey@enron.com',
 'gerald.nemec@enron.com',
 'greg.whalley@enron.com',
 'harry.arora@enron.com',
 'holden.salisbury@enron.com',
 'james.derrick@enron.com',
 'jane.tholt@enron.com',
 'jason.williams@enron.com',
 'jason.wolfe@enron.com',
 'jay.reitmeyer@enron.com',
 'jeff.dasovich@enron.com',
 'jeff.king@enron.com',
 'jeff.skilling@enron.com',
 'jeffrey.shankman@enron.com',
 'jim.schwieger@enron.com',
 'joe.parks@enron.com',
 'joe.quenet@enron.com',
 'joe.stepenovitch@enron.com',
 'john.arnold@enron.com',
 'john.griffith@enron.com',
 'john.hodge@enron.com',
 'john.lavorato@enron.com',
 'john.zufferli@enron.com',
 'jonathan.mckay@enron.com',
 'judy.hernandez@enron.com',
 'judy.townsend@enron.com',
 'kam.keiser@enron.com',
 'kate.symes@enron.com',
 'kay.mann@enron.com',
 'keith.holst@enron.com',
 'kenneth.lay@enron.com',
 'kevin.hyatt@enron.com',
 'kevin.ruscitti@enron.com',
 'kim.ward@enron.com',
 'kimberly.watson@enron.com',
 'larry.campbell@enron.com',
 'larry.may@enron.com',
 'legal <.taylor@enron.com>',
 'lindy.donoho@enron.com',
 'lisa.gang@enron.com',
 'liz.taylor@enron.com',
 'louise.kitchen@enron.com',
 'lynn.blair@enron.com',
 'lysa.akin@enron.com',
 'm..forney@enron.com',
 'm..presto@enron.com',
 'marie.heard@enron.com',
 'mark.guzman@enron.com',
 'mark.whitt@enron.com',
 'martin.cuilla@enron.com',
 'mary.fischer@enron.com',
 'matt.motley@enron.com',
 'matt.smith@enron.com',
 'matthew.lenhart@enron.com',
 'michelle.cash@enron.com',
 'michelle.lokay@enron.com',
 'mike.carson@enron.com',
 'mike.grigsby@enron.com',
 'mike.maggi@enron.com',
 'mike.mcconnell@enron.com',
 'mike.swerzbin@enron.com',
 'monika.causholli@enron.com',
 'monique.sanchez@enron.com',
 'patrice.mims@enron.com',
 "paul.y'barbo@enron.com",
 'peter.keavey@enron.com',
 'phillip.allen@enron.com',
 'phillip.love@enron.com',
 'phillip.platter@enron.com',
 'randall.gay@enron.com',
 'richard.ring@enron.com',
 'richard.shapiro@enron.com',
 'rick.buy@enron.com',
 'robert.badeer@enron.com',
 'robert.benson@enron.com',
 'robin.rodrigue@enron.com',
 'rod.hayslett@enron.com',
 'ryan.slinger@enron.com',
 's..shively@enron.com',
 'sally.beck@enron.com',
 'sara.shackleton@enron.com',
 'scott.hendrickson@enron.com',
 'scott.neal@enron.com',
 'sean.crandall@enron.com',
 'shelley.corman@enron.com',
 'stacy.dickson@enron.com',
 'stanley.horton@enron.com',
 'stephanie.panus@enron.com',
 'steven.kean@enron.com',
 'steven.merris@enron.com',
 'steven.south@enron.com',
 'susan.bailey@enron.com',
 'susan.scott@enron.com',
 't..lucci@enron.com',
 'tana.jones@enron.com',
 'teb.lokey@enron.com',
 'theresa.staab@enron.com',
 'thomas.martin@enron.com',
 'tom.donohoe@enron.com',
 'tori.kuykendall@enron.com',
 'tracy.geaccone@enron.com',
 'v.weldon@enron.com',
 'vince.kaminski@enron.com',
 'vladi.pimenov@enron.com',
 'w..pereira@enron.com',
 'w..white@enron.com']
            
    if (not os.path.isdir(fileName)):        
        with open(fileName,'r', encoding= 'cp1252') as f:
                 f_contents=f.readlines()
                   
                
                 
                 blocks=f_contents[1].split()
                 for thing in blocks: 
                     for i in range(1,13):
                                
                         if thing == parseSingleEmail.month[i]:
                                        
                             blocks[3]=str(i)
                             temp_date=', '.join(blocks[2:5])
                             email_date=datetime.strptime(temp_date ,'%d, %m, %Y')
                             
                             
                 
                 g=3
                 if (email_date>=start_date and email_date<=end_date):
                      inEmails=0
                      while(not("Subject:" in f_contents[g]) and inEmails !=1):

                                  
                                   
                                        f_contents[g].strip('\t')
                                        
                                        
                                        temp=f_contents[g].split(',')
                                        for employee in temp:
                                            employee = employee.strip()
                                            if(employee != '' and employee in emails):
                                                    inEmails=1
                                                    break
                                            else:
                                                inEmails=2
                                        g=g+1                
                      if(inEmails==1):
                                        
                    
                         if('Date' in value):
                                 parseSingleEmail.email['Date'].append(email_date)
                                 
                         r=3        
                         if 'To' or 'From' in value:
                                
                                while(not("Subject:" in f_contents[r])):
                                       
                                      
                                       
                                            f_contents[r].strip('\t')
                                            
                                            
                                            temp=f_contents[r].split(',')
                                            
                                            
                                            for employee in temp:
                                                employee = employee.strip()
                                                if(employee != ''):
                                               
                                                   f_contents[2]=f_contents[2].strip('\n')
                                                   f_contents[2]=f_contents[2].replace('From: ','')
                                                   
                                                   
                                                   
                                                   employee=employee.strip()
                                                   employee=employee.replace('To: ','')
                                                  
                                                   
    
                                                          
                    
                                                   if 'To' in value:
                                                       parseSingleEmail.email['To'].append(employee)   
                                                   
                                                   
                                                   
                                                   
                                                   if 'From' in value:
                                                       parseSingleEmail.email['From'].append(f_contents[2])
                                            
                                            
                                       
                                            r=r+1
                         if 'Subject' in value:
                            for line in f_contents:
                                if 'Subject:' in line:
                                    line=line.replace("Subject: ", "").replace("Re: ", "").replace("RE: ", "").replace("FW: ", "").replace("FW:", "").replace("Re:", "").replace("Subject:", "").replace("RE:", "")
                                    
                                    
                                    line=line.strip('\n')
                                    
                                    parseSingleEmail.email['Subject'].append(line)
                                    
                                    
                                    break
                         body=''
                         if 'Body' in value :
                            x=  f_contents.index('\n')
                            for i in  range(x,len(f_contents)):
                                body=body+ f_contents[i]
                            parseSingleEmail.email['Body'].append(body)
                       
                    
                          
    return parseSingleEmail.email
def parseAllEmails(folderName, value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return parsed sections-Date, Subject, To, From,Body-  of all the emails
    
    
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
    parseAllEmails.allEmails=defaultdict(list) 
    
    file=os.listdir(folderName)
    if(type(all_sent) is not list):
        all_sent=[all_sent]
    for item in file:
        if os.name == 'posix' :  
            userEmail = parseUserEmails(folderName+'/'+item,value,all_sent,start_date,end_date)
            
        else:
            userEmail = parseUserEmails(folderName+'\\'+item,value,all_sent,start_date,end_date)
            
        if len(userEmail['Subject']) > 0:
            parseAllEmails.allEmails['Subject']=parseAllEmails.allEmails['Subject']+(userEmail['Subject'])
                      
        if len(userEmail['To'])>0 or len(userEmail['From'])>0:
            parseAllEmails.allEmails['To']=parseAllEmails.allEmails['To']+(userEmail['To'])
            
                     
        if len(userEmail['From'])>0:
            parseAllEmails.allEmails['From']=parseAllEmails.allEmails['From']+(userEmail['From'])
                      

        
        if len(userEmail['Body']) >0:
            parseAllEmails.allEmails['Body']=parseAllEmails.allEmails['Body']+(userEmail['Body'])
        if len(userEmail['Date'])>0:
            parseAllEmails.allEmails['Date']=parseAllEmails.allEmails['Date']+(userEmail['Date'])

    return parseAllEmails.allEmails
def parseUserEmails(folderName, value=['Subject','Date','To', 'From','Body'],all_sent=['sent','_sent_mail','sent_items','_sent'],start_date='1 1 1998',end_date='31 12 2002'):
    """Return parsed sections-Date, Subject, To, From,Body-  of a single user
    
    
    
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
    parseUserEmails.userEmails=defaultdict(list) 
    
    if(type(all_sent) is not list):
        all_sent=[all_sent]    
    
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
                       u=parseSingleEmail(sent_email +"/"+email,value,start_date,end_date)
                       
                 else:
                       u=parseSingleEmail(sent_email +"\\"+email,value,start_date,end_date)
                       
                  
                 
                 
                  
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