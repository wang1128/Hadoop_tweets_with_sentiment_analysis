#!/usr/bin/env python

from operator import itemgetter
import sys

current_tweet = None
current_rank = 0
tweet = None

# input comes from STDIN
for line in sys.stdin:

    line = line.strip()


    tweet, rank = line.split(',')


    try:
        rank = float(rank)
    except ValueError:

        continue


    if current_tweet == tweet:
        current_rank += rank
    else:
        if current_tweet:
            # write result to STDOUT
            print(current_tweet, current_rank)
        current_rank = rank
        current_tweet = tweet
if current_tweet == tweet:
    print (current_tweet, current_rank)