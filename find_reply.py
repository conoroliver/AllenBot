#Author: Conor Oliver
#5 July 2017

import praw
import pdb
import re
import os

#reddit = praw.Reddit('bot1')

def find_and_reply(subreddits, reddit):
    """
    Takes a list of subreddits (strings) and will monitor those subreddits, replying to chosen comments
    """

    # GO THROUGH COMMENTs
    comment_count = 0
    subreddit = reddit.subreddit("ripcity")
    with open("comments_replied_to_" + str(subreddits[0]) + ".txt", "w+") as f, open("comments_replied_to_" +
                    str(subreddits[0]) + "_text.txt", "w+") as f2, open("comments_replied_to_" + str(subreddits[1]) +
                    ".txt", "w+") as f3, open("comments_replied_to_" + str(subreddits[1]) + "_text.txt", "w+") as f4:
        # f2.write(str(comment_count) + " comments evaluated\n")
        # print comment_count
        comments_replied_to = f.read() + f3.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

        for comment in reddit.subreddit("nba+ripcity").stream.comments():
            comment_count += 1
            if comment.subreddit == subreddits[0]:
                if comment not in comments_replied_to and should_reply(comment, comment.subreddit):
                    f.write(str(comment) + "\n")
                    comments_replied_to.append(str(comment))
                    f2.write(comment.body.encode('utf-8') + ",")

            if comment.subreddit == subreddits[1]:
                if comment not in comments_replied_to and should_reply(comment, comment.subreddit):
                    f3.write(str(comment) + "\n")
                    f4.write(comment.body.encode('utf-8') + ",")

    print len(comments_replied_to)


def should_reply(comment, subreddit):
    """
    Takes a comment and determines whether or not it should be replied to.
    This function parses comments, looking for certain keywords that would warrant a reply
    """
    cmt_text = comment.body.encode('utf-8').strip()
    eval_score = 0

    num_test_words = float(12)

    found_list = re.findall(r"luxury tax|salary dump|bad contract", cmt_text, re.IGNORECASE)
    found_list = list(set(found_list))

    for match in found_list:
        eval_score += 3

    if subreddit == "nba":
        if not re.findall(r"blazer|lillard|ripcity|allen", cmt_text, re.IGNORECASE):
            return False



    for word in cmt_text.split():
        if re.search(r"crabbe|turner|over|dump|trade|too|cap|salary", word, re.IGNORECASE):
            eval_score += 1

    print "hey blazer " + str(comment.subreddit) + "with a score of  " + str(eval_score) + ":\n" + cmt_text + "\n"
    if eval_score >= 1:
        return True

    return False
