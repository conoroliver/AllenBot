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
    if not os.path.isfile("comments_replied_to_" +str(subreddits[0])+".txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to_" +str(subreddits[0])+".txt", "rw") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    if not os.path.isfile("comments_replied_to_" + str(subreddits[1]) + ".txt"):
        comments_replied_to2 = []
    else:
        with open("comments_replied_to_" + str(subreddits[1]) + ".txt", "rw") as f:
            comments_replied_to2 = f.read()
            comments_replied_to2 = comments_replied_to2.split("\n")
            comments_replied_to2 = list(filter(None, comments_replied_to2))

    initial_length = len(comments_replied_to)
    # GO THROUGH COMMENTS
    new_comments = []
    new_comments2 = []
    comment_count = 0
    for comment in reddit.subreddit(subreddits[0]).stream.comments():
        comment_count += 1
        if comment.subreddit == subreddits[0]:
            if comment not in comments_replied_to and should_reply(comment, comment.subreddit):
                print "new comment found"
                comments_replied_to.append(comment)
                new_comments.append(comment)
        if comment.subreddit == subreddits[1]:
            if comment not in comments_replied_to and should_reply(comment, comment.subreddit):
                print "new comment found"
                comments_replied_to2.append(comment)
                new_comments2.append(comment)

    print len(comments_replied_to)
    with open("comments_replied_to_" + str(subreddits[0]) + ".txt", "w+") as f:
        for comment in new_comments:
            f.write(str(comment) + "\n")

    with open("comments_replied_to_" + str(subreddits[0]) + "_text.txt", "w+") as f2:
        # f2.write(str(comment_count) + " comments evaluated\n")
        # print comment_count
        for comment in new_comments:
            f2.write(comment.body.encode('utf-8') + ",")

    with open("comments_replied_to_" + str(subreddits[1]) + ".txt", "w+") as f:
        for comment in new_comments2:
            f.write(str(comment) + "\n")

    with open("comments_replied_to_" + str(subreddits[1]) + "_text.txt", "w+") as f2:
        # f2.write(str(comment_count) + " comments evaluated\n")
        # print comment_count
        for comment in new_comments2:
            f2.write(comment.body.encode('utf-8') + ",")


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
        if not re.findall(r"blazer", cmt_text, re.IGNORECASE):
            return False

    print "hey blazer"

    for word in cmt_text.split():
        if re.search(r"crabbe|turner|over|dump|trade|too|cap|salary", word, re.IGNORECASE):
            eval_score += 1

    if eval_score >= 4:
        return True

    return False
