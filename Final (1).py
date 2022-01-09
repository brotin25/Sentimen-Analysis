#!/usr/bin/env python
# coding: utf-8

# In[33]:


import difflib as dl
import re
import nltk
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import text2emotion as te
import demoji
from nltk.corpus import wordnet


import math
from collections import Counter

f = open('twitter.txt', 'r')
stop=[]
l = []
for l in f:
        stop.append(l.strip())

nt=2920
#nt=310
urls=[]
urlt = 'http[s]?://(?:[a-zA-Z]|0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
WORD = re.compile(r'\w+')
hashtags=[]
username=[]
tweet=[]
cluster=1
cluster1=1
Lmax=140
final_tweet=[]
node_from=[]
node_to=[]
node_weight=[]


# In[34]:





# In[35]:


#Remove usernames
def removal(data):
 
        data = re.sub(r'\d+', '', data)
        data = re.sub(r'(.)\1+', r'\1\1', data)
        data= re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?л╗УФСТ]))', '',data)
        data= re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",data)
        punc = list('!"#$%&\'()*+,-./:;<=>?[\\]^_`{|}~')
        for line in data:
                 if line in punc:
                         data = data.replace(line,'')	
        hashtag = list("@[A-Za-z0-9_]+")
        data = data.replace('&amp;','')
        data = data.replace('&nbsp;',' ')
        data = data.replace('&lt;',' ')
        data = data.replace('&rt;',' ')
        data = re.sub('[\s]+', ' ', data)
        
        
        return data
print (removal(str(stop)))


# In[39]:


import pandas as pd

def filtertweet (data):
    import pandas as pd

def filtertweet ():
    mylines = []                              # Declare an empty list
    pos=[]
    neg=[]
    Descision =[]
    spilit_word_line=[]
    with open ('twitter.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:                   # For each line of text,
            mylines.append(line)              # add that line to the list.
        for element in mylines:        
            if element[0]<element[2]:
                Descision.append("Postive")
            else:
                Descision.append("Negative")
        for i in mylines:            
            spilit_word_line.append(i.split(" "))
        for i in spilit_word_line:
            syn=wordnet.synset(i)
            print(syn[0].lemmas()[0].name())           #positive []= sp

            

i=0
with open('twitter.txt') as f:
    lines=f.readlines()
for l in lines:
    l=userem(l)
    t=l.split(' ') 
    print (t)
    break


# In[2]:


import re
import math
from collections import Counter
import nltk
from nltk.tag import pos_tag_sents 
nltk.download('wordnet') 
nltk.download('omw-1.4')
from nltk.corpus import wordnet
f = open('twitter.txt', 'r')
stop=[]
l = []
for l in f:
        stop.append(l.strip())

nt=2920
#nt=310
urls=[]
urlt = 'http[s]?://(?:[a-zA-Z]|0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
WORD = re.compile(r'\w+')
hashtags=[]
username=[]
tweet=[]
cluster=1
cluster1=1
Lmax=140
final_tweet=[]
node_from=[]
node_to=[]
node_weight=[]

mylines = []                              # Declare an empty list
pos=[]
neg=[]
postive_word_count=[]
negative_word_count=[]
Descision =[]
spilit_word_line =[]
with open ('twitter.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
    for line in myfile:                   # For each line of text,
        mylines.append(line)              # add that line to the list.
    for element in mylines:       
        if element[0]<element[2]:
            Descision.append("Positive")
        else:
            Descision.append("Negative")
for i in mylines:            
    spilit_word_line.append(i.split(" "))
# for i in spilit_word_line:
#     syn=wordnet.synsets(str(i[0]))
j=0
positivecount=[]
negativecount=[]
positive_counter_index =0
negative_counter_index =0
pcount=0
ncount=0
lineno=0
n=0
p=0

for i in spilit_word_line:
    for k in i :
        word = k
        word=word.split(' ')

        syn=wordnet.synsets(str(word[0]))
        if(len(syn)): 
            for l in mylines:
                if(l.find(word[0])!=-1):
                    desc_line=Descision[lineno]
                    if(desc_line == "Positive"):
                        pcount+=1
                        positivecount.insert(positive_counter_index,int(pcount))
                    if(desc_line == "Negative"):
                        ncount+=1
                        negativecount.insert(negative_counter_index,int(ncount))
                lineno+=1
            positive_counter_index+=1
            negative_counter_index+=1
            pcount=0
            ncount=0
        lineno=0            
        n=0
        p=0

i = 0 
result=[]
for k in positivecount:
    if k > negativecount[i]:
        result.append("Positive")
    else:
        result.append("Negetive")
    i+=1
print (result)


# In[44]:





# In[66]:





# In[1]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




