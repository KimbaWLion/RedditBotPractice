#!/usr/bin/python
import sys
import time
import praw

def wait_2_seconds():
    waittime = 2
    print 'Wait {0} seconds because you cannot make a call more than once every 2 seconds'.format(waittime)
    time.sleep(waittime)
    print 'Now actually start the program'
    sys.stdout.flush()




wait_2_seconds()

user_agent = ("PyEng Bot 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("learnpython")

#print subreddit
"""for submission in subreddit.get_hot(limit = 5):
    print submission"""

for submission in subreddit.get_hot(limit = 5):
    print "Title: ", submission.title
    print "Text: ", submission.selftext
    print "Score: ", submission.score
    print "---------------------------------\n"