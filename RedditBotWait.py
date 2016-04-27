#!/usr/bin/python
import time
import sys

def wait_2_seconds():
    wait_seconds(2)

def wait_2_seconds_no_display():
    wait_seconds(2,False)

def wait_seconds(waittime, display=True):
    if display:
        print 'Wait {0} seconds because you cannot make a call more than once every 2 seconds'.format(waittime)
    time.sleep(waittime)
    if display:
        print 'Now actually start the program'
    sys.stdout.flush()