"""
Bot to organize your saved posts. It writes your post, and the post url to a files called
[subreddit].txt in a direcotry called 'Saved_Posts which is created wherever you want it.
Posts are organized by subreddit.
"""

import praw
import argparse
import os
 
parser = argparse.ArgumentParser()
parser.add_argument('username', help="Your reddit username")
parser.add_argument('password', help="Your reddit password")
parser.add_argument('directory', 
                    help="The directory you want me to check for saved"+
                    " posts example: /home/user/reddit")
 
args = parser.parse_args()
 
r = praw.Reddit(user_agent="Get saved posts")
r.login(args.username, args.password)
 
for post in r.user.get_saved():
    sub = post.subreddit.display_name
    flag = 0
    
    os.chdir(args.directory)
    for i in os.listdir(os.getcwd()):
        if os.path.isdir(i):
            if i == 'Saved_Posts':
                flag = 1
                break
 
    if flag == 0:
        os.makedirs('Saved_Posts')
    
    os.chdir('Saved_Posts')
 
    f = open(sub+'.txt','a')
    try:
        if post.body:
            pass
 
        f.write(post.submission.title+'\n')
        f.write(post.submission.url+'\n')
        f.write('\n')
    
    except AttributeError:
        f.write(post.title+'\n')
        f.write(post.url+'\n')
        f.write('\n')
    
    post.unsave()
    f.close()
