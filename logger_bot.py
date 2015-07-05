#!/usr/bin/env python

import praw
import time

r = praw.Reddit('Program to analyse the most accurate predictor')

#Type your subreddit and words here below
REDDIT = 'pcmasterrace'
words = ['input', 'demand', 'version', 'arkham', 'light']
comment_words = ['speed', 'glorious', 'pcmr', 'gaben', 'praise']
r.login()

taken = []
f = open('logger.txt', 'w')

while True:
    sub = r.get_subreddit(REDDIT)
    """Modify the limit of submission too if needed"""
    for submission in sub.get_hot(limit=10):
        sub_text = submission.title.lower()
        has_words = any(string in sub_text for string in words)
        print has_words

        if submission.id not in taken and has_words:
            submission.replace_more_comments(limit=None, threshold=0)
            flat_comments = praw.helpers.flatten_tree(submission.comments)
            already = set()  
            for comment in flat_comments:
                has = any(string in comment.body for string in words)
                print 'has', has
                if comment.id not in already and has:

                    """Get the author of the comment that matches and write to file"""
                    au = comment.author
                    already.add(comment.id)
                    f.write('www.reddit.com/user/' + au.name + '\n')
     
