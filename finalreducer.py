#!/usr/bin/env python

from operator import itemgetter
import sys

current_tweet = None
current_rank = 0
tweet = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    tweet, rank = line.split(',')

    # convert count (currently a string) to int
    try:
        rank = int(rank)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
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