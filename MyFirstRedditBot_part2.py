#!/usr/bin/python
import sys
import RedditBotWait
import praw
import pdb
import re
import os
from config_bot import *

RedditBotWait.wait_2_seconds()

# Check that the file that contains our username exists
if not os.path.isfile("config_bot.py"):
    print "You must create a config file with your username and password."
    print "Please see config_skel.py"
    exit(1)

# Create the Reddit instance
user_agent = ("PyFor Eng bot 0.1")
r = praw.Reddit(user_agent=user_agent)

# and login
r.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

# Get the top 5 values from our subreddit
subreddit = r.get_subreddit('pythonforengineers')
try:
    for submission in subreddit.get_new(limit=5):
        RedditBotWait.wait_2_seconds_no_display()  # Wait 2 seconds for each call
        print "Submission title :",submission.title

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            if re.search("i love python", submission.title, re.IGNORECASE):
                # Reply to the post
                submission.add_comment("Who believes in doing good and doing right?\n\nKimba the white lion is the one!")
                print "Bot replying to : ", submission.title

                # Store the current id into our list
                posts_replied_to.append(submission.id)
        else:
            print "Replied to ", submission.title, "already"
except praw.errors.RateLimitExceeded as e:
    print "User not verified, cannot make comments within 10 minutes of each other. Error message :", e.message
finally:
    # Write our updated list back to the file
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")