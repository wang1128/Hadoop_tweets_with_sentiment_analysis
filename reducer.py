__author__ = 'penghao'
#!/usr/bin/env python


import sys
from textblob import TextBlob


f2 = open("in.txt","r")
a1 = f2.readlines()
totallist=[]
'''
for w in a:
    totallist.append(w)
print(w)'''
# input comes from STDIN
for line in a1:
    # remove leading and trailing whitespace
    words = line.split(',')
    number = words[2].strip(')\n')
    number=number.strip("'")
    number=number.strip(" '")
    print(int(number))
    if int(number) >1000:
        print(words[0],words[1])
    if 'love' in words[1]:
        print("good")
        print(words[1])
    #print(words[1])
    #blob = TextBlob(words[1])
    #sentiment=0
    #for sentence in blob.sentences:
    #    sentiment = sentiment + sentence.sentiment.polarity

    #print(words[0], sentiment)




