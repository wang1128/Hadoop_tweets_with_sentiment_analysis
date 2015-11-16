__author__ = 'penghao'

import sys
from textblob import TextBlob

f = open("test.txt","r")
a = f.readlines()
# input comes from STDIN (standard input)
totallist=[]
count=0
for line in a:
    # remove leading and trailing whitespace
    #line = line.strip()
    # split the line into words
    words = line.split(',')
    # increase counters
    list=[]
    for word in words:

        word = word.split(':')
        if word[0] == '{"created_at"':

            count=count+1
            list.append(word)
        if word[0] == '"text"'  or word[0] == '"followers_count"' or word[0] == '"retweet_count"':
            list.append(word)
    if(list!=[]):
        totallist.append(list)



for tweet in totallist:
    #follower count
    if tweet[0][0] == '{"created_at"':
        print(tweet[0][1],tweet[1][1]+tweet[1][2],tweet[2][1])
        #print(tweet[1])
    blob = TextBlob(tweet[1][2])
    #for sentence in blob.sentences:
    #    print(sentence.sentiment.polarity)