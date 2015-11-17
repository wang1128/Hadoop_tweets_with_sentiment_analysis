#!/usr/bin/env python

from operator import itemgetter
import sys

current_tweet = None
current_rank = 0
tweet = None
count =1
# input comes from STDIN
for line in sys.stdin:

    line = line.strip()


    tweet, rank ,followers= line.split(',')


    try:
        rank = float(rank)
    except ValueError:

        continue


    if current_tweet == tweet:
        current_rank += rank
        count = count + 1

    else:
        if current_tweet:
            # write result to STDOUT
            ave= current_rank/count
            print(current_tweet, current_rank)
        current_rank = rank
        current_tweet = tweet
        count = 1
if current_tweet == tweet:
    print (current_tweet, current_rank)