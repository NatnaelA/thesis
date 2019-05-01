# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:40:28 2019

@author: Natna
"""





from collections import defaultdict


from datetime import datetime
def parseSingleEmail(fileName,value=['Subject','Date','To', 'From','Body']):
    """Return parsed sections-Date, Subject, To, From,Body-for a single email
    
    
    value: the different section of the email
           can be user specified
           default to ['Subject','Date','To', 'From','Body']
   
    """
    parseSingleEmail.month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    parseSingleEmail.email = defaultdict(list)
    parseSingleEmail.flag2=None
    parseSingleEmail.flag=None
    #parseEmail.email.clear()
    
       
    
#    if('start_date' not in value):
#
#        start_date=datetime.strptime( '1, 1, 1998','%d, %m, %Y')
#
# 
#
#    if('end_date' not in value):
#
#        end_date=datetime.strptime('31, 12, 2002','%d, %m, %Y')
    for item in value:
       
        if type(item)==dict and 'Start_Date' in item and 'End_Date' in item :
           
            temp_start=item['Start_Date'].split()
            temp_end=item['End_Date'].split()
           
            if (parseSingleEmail.flag2)==None:
                temp_start=item['Start_Date'].split()
                temp_end=item['End_Date'].split()
                item['Start_Date']=', '.join(temp_start)
                item['End_Date']=', '.join(temp_end)
                parseSingleEmail.flag2=True
            start_date=datetime.strptime( item['Start_Date'],'%d, %m, %Y')
            end_date=datetime.strptime( item['End_Date'],'%d, %m, %Y')
            
            parseSingleEmail.flag=True
            break
            
        elif type(item)==dict and'Start_Date' in item and 'End_Date' not in item:
          
            
            
            
            if parseSingleEmail.flag2==None:
                temp_start=item['Start_Date'].split()
                item['Start_Date']=', '.join(temp_start)
                parseSingleEmail.flag2=True
            start_date=datetime.strptime( item['Start_Date'],'%d, %m, %Y')
            end_date=datetime.strptime('31, 12, 2002','%d, %m, %Y')
            parseSingleEmail.flag=True
            break
        elif type(item)==dict and 'Start_Date' not in item and 'End_Date' in item:
            
            print('it goes here3')
           
            
            if parseSingleEmail.flag2==None:
                temp_end=item['End_Date'].split()
                item['End_Date']=', '.join(temp_end)
                parseSingleEmail.flag2=True
            start_date=datetime.strptime( '1,1,1998','%d, %m, %Y')
            end_date=datetime.strptime(item['End_Date'],'%d, %m, %Y')
            parseSingleEmail.flag=True
            break
    if parseSingleEmail.flag == None:
            
            start_date=datetime.strptime( '1, 1, 1998','%d, %m, %Y')
            end_date=datetime.strptime('31, 12, 2002','%d, %m, %Y')
            
            
    with open(fileName,'r') as f:
             f_contents=f.readlines()
               
            
             
             blocks=f_contents[1].split()
             for thing in blocks: 
                 for i in range(1,13):
                            
                     if thing == parseSingleEmail.month[i]:
                                    
                         blocks[3]=str(i)
                         temp_date=', '.join(blocks[2:5])
                         email_date=datetime.strptime(temp_date ,'%d, %m, %Y')
                         
                         
             
             r=3
             if (email_date>=start_date and email_date<=end_date):
                
                 if('Date' in value):
                         parseSingleEmail.email['Date'].append(email_date)
                         
                         
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
                           # line=line.replace("Subject: ", "")
                            
                            parseSingleEmail.email['Subject'].append(line)
                            
                            
                            break
                 body=''
                 if 'Body' in value:
                    x=  f_contents.index('\n')
                    for i in  range(x,len(f_contents)):
                        body=body+ f_contents[i]
                    parseSingleEmail.email['Body'].append(body)
                   
                    
                          
    return parseSingleEmail.email
