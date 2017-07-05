#Author: Conor Oliver
#5 July 2017

import praw
import pdb
import re
import os

replies_checked = False


def check_replies():
    if not os.path.isfile("comments_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
    replies_checked = True;


def find_and_reply(subreddit):
    if not replies_checked:
        check_replies()
    for comment in subreddit.comments(limit=1):
        if should_reply(comment):
            # reply
            print "true"


def should_reply(comment, subreddit):
    """
    Takes a comment and determines whether or not it should be replied to.
    This function parses comments, looking for certain keywords that would warrant a reply
    """
    cmt_text = str(comment.body)
    print cmt_text
    eval_score = 0
    for word in cmt_text.split():
        print word
    if eval_score > 4:
        return True
    return False
