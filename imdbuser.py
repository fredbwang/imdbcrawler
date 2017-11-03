# -*- coding: utf-8 -*-

import pandas as pd
import urllib2
import time
import lxml.html
from pandas import DataFrame
doubanMovie_info=pd.read_csv('IMDBfinal3.csv')    
IMDBurl=doubanMovie_info['IMDBRate']    
IMDBRateList=[]  
nameList=[]

def getDoc(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    request = urllib2.Request('http://www.imdb.com'+url+'reviews?start=0', headers=headers)  # send request
    response = urllib2.urlopen(request)  # get response
    #time.sleep(1)
    content = response.read()  # get web content
    doc = lxml.html.fromstring(content)  
    return doc
def getDoc2(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    request = urllib2.Request('http://www.imdb.com'+url+'reviews?start=10', headers=headers)  
    response = urllib2.urlopen(request)  
    #time.sleep(1)
    content = response.read() 
    doc = lxml.html.fromstring(content)  
    return doc
def getDoc3(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    request = urllib2.Request('http://www.imdb.com'+url+'reviews?start=20', headers=headers) 
    response = urllib2.urlopen(request)  
    #time.sleep(1)
    content = response.read()
    doc = lxml.html.fromstring(content) 
    return doc
#函数：获得IMDB评分
def getIMDBRate(doc,oneIMDBurl):
    #匹配IMDB评分的xpath路径
    temp1=[]
    temp2=[]
    if doc.xpath('//*[@id="tn15content"]/div[1]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[1]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[1]/a/text()')[0])
    if doc.xpath('//*[@id="tn15content"]/div[3]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[3]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[3]/a/text()')[0])
    if doc.xpath('//*[@id="tn15content"]/div[5]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[5]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[5]/a/text()')[0])
    if doc.xpath('//*[@id="tn15content"]/div[7]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[7]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[7]/a/text()')[0])
    if doc.xpath('//*[@id="tn15content"]/div[9]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[9]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[9]/a/text()')[0])
    if doc.xpath('//*[@id="tn15content"]/div[11]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[11]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[11]/a/text()')[0])
    if doc.xpath('//*[@id="tn15content"]/div[13]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[13]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[13]/a/text()')[0])
    if doc.xpath('//*[@id="tn15content"]/div[15]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[15]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[15]/a/text()')[0])
    if doc.xpath('//*[@id="tn15content"]/div[17]/a/@href'):
    	temp1.append(doc.xpath('//*[@id="tn15content"]/div[17]/a/@href')[0])
    	temp2.append(doc.xpath('//*[@id="tn15content"]/div[17]/a/text()')[0])
    #print temp1
    #print temp2
    return temp1, temp2   # return string


def toInt(numWithDot):
    temp1=numWithDot.split(',') 
    temp2=''
    for i in range(len(temp1)):    
        temp2+=temp1[i]
    temp2=int(temp2)   
    return temp2

# get rate user name
def getNumOfPeopleWhoRate(doc,oneIMDBurl):
    
    tempList=doc.xpath('//*[@id="titleUserReviewsTeaser"]/div[1]/span/div[1]/a/span/text()')
    print tempList[0]
    return tempList[0]   

num=1   
startPoint=1
for i in range(startPoint-1,len(IMDBurl)):
    print i+1   
    try:
       
        if IMDBurl[i]!='-':    # if this movie exists
            doc=getDoc(IMDBurl[i])    
            doc2=getDoc2(IMDBurl[i])
            doc3=getDoc3(IMDBurl[i])
            #得到IMDB评分
            IMDBRate,name=getIMDBRate(doc,IMDBurl[i])
            for i in range(len(IMDBRate)):
            	IMDBRateList.append(IMDBRate[i])
            	nameList.append(name[i])
            IMDBRate,name=getIMDBRate(doc2,IMDBurl[i])
            for i in range(len(IMDBRate)):
            	IMDBRateList.append(IMDBRate[i])
            	nameList.append(name[i])
            IMDBRate,name=getIMDBRate(doc3,IMDBurl[i])
            for i in range(len(IMDBRate)):
            	IMDBRateList.append(IMDBRate[i])
            	nameList.append(name[i])
            #IMDBRateList.append(IMDBRate)    
          
            #name=getNumOfPeopleWhoRate(doc,IMDBurl[i])
            #nameList.append(name)    
        else:   
            print 'Movie:',i+1,'Without IMDBurl,No.',num  
            num=num+1    
            IMDBRateList.append('-')
            nameList.append('-')
    except:    
        print 'unknownError happened!'
        #IMDBRateList.append('unknownError')
        #nameList.append('unknownError')
    finally:
        
        IMDBRate=DataFrame({'IMDBRate':IMDBRateList,'name':nameList})  
       
        IMDBRate.to_csv('IMDBallusers3.csv',index=False,encoding='utf-8')
