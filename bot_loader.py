#Author: Conor Oliver
#5 July 2017

import praw
import find_reply


reddit = praw.Reddit('bot1')

subreddits = []

ripcity = reddit.subreddit("ripcity")
subreddits.append(ripcity)

nba = reddit.subreddit("nba")
subreddits.append(nba)

find_reply.find_and_reply(subreddits, reddit)