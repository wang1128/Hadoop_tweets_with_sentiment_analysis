#!/usr/bin/env python
import sys
from textblob import TextBlob
import nltk
#author: Penghao Wang

totallist=[]
count=0
for line in sys.stdin:

    try:
        line = line.strip()

        words = line.split(',')

        list=[]
        for word in words:
            word = word.split(':')
            if word[0] == '{"created_at"':
                count=count+1
                list.append(word)
            if word[0] == '"text"'  or word[0] == '"followers_count"' or word[0] == '"location"' or word[0] == '"retweet_count"' or word[0] == '"favorite_count"':
                list.append(word)
        if(list!=[]):
            totallist.append(list)
    except ValueError:
        continue
for tweet in totallist:

    try:
        if tweet[0][0] == '{"created_at"' and len(tweet[1])>=4:
            t=tweet[1][1]+tweet[1][2]+tweet[1][3]
            blob = TextBlob(t)
            sentiment=blob.sentiment.polarity
            #for sentence in blob.sentences:
            #    sentiment = sentiment + sentence.sentiment.polarity
            print(tweet[0][1],sentiment,tweet[2][1])
        if tweet[0][0] == '{"created_at"' and len(tweet[1])==3:
            t=tweet[1][1]+tweet[1][2]
            blob = TextBlob(t)
            sentiment=blob.sentiment.polarity
            #for sentence in blob.sentences:
            #    sentiment = sentiment + sentence.sentiment.polarity
            print(tweet[0][1],sentiment,tweet[2][1])
    except ValueError:
        continue