#Author: Conor Oliver
#5 July 2017

import praw
import find_reply

reddit = praw.Reddit('bot1')

ripcity = reddit.subreddit("ripcity")

nba = reddit.subreddit("nba")

find_reply.find_and_reply(nba)