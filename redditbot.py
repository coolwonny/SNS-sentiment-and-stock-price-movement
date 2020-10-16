import os
import praw
import datetime as dt
import pandas as pd

#create reddit object
reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     password=os.getenv("REDDIT_PASSWORD"),
                     user_agent=os.getenv("REDDIT_USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))

for sub in ['teslamotors', "elonmusk"]:
    posts = []
    after = ''
    last_record = ' '

    # while loop gets around reddit limit of records returned
    while after != last_record:
        last_record = after
        submissions = reddit.subreddit(sub).new(limit=None, params={"after": after})
        for submission in submissions:
            try:
                posts.append({
                    "author":submission.author,
                    "subreddit":submission.subreddit,
                    "date": dt.datetime.utcfromtimestamp(submission.created),
                    "text": submission.title,
                    "id": submission.id
                })
            except AttributeError:
                pass
            after = submission.fullname
    
    # Gather submissions and create the dataframe    
    df = pd.DataFrame(posts, columns=["author", "subreddit", "date", "text", "id"])
    # write to file
    df.to_csv(f'reddit_r_{sub}.csv', sep='DELIMITER', index=False, encoding="utf-8")