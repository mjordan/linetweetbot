#!/usr/bin/env python

from twitter import *

"""
Config variables
"""

# Set up authentication for this Twitter app.
oa_access_token = 'samplee320asuyiuwepjdiwu2'
oa_access_token_secret = 'samplemnbxcpw8383'
consumer_key = 'samplepekdncisyqgeq8d44d'
consumer_secret = 'sampleooojwydcw53ip'

# We read and write to the same data file, popping the first
# line off it and tweeting that line. If your data file is not
# in the same directory as this script, use a full path.
data_file_name = 'data.txt'

# String tacked onto the end of tweets to indicate that the 
# sentence is comprised of multiple tweets.
tweet_separator = ' [...]' 

"""
Functions
"""

def get_chunks(line):
    """
    Breaks lines up into chunks of a maximum of 140 characters long.
    However, we need to subtract the length of tweet_separator so we 
    can include it in tweets that contain partial sentences.

    Note that this function limits line length on character
    count, not word count, so we will get words split over
    multiple tweets. Looks bad but I am lazy.
    """
    chunk_length = 140 - len(tweet_separator)
    line_length = len(line)

    # If the line fits in one tweet, return it here.
    if line_length < 140:
        return [line]

    # In the script's main logic, we loop through this list and tweet
    # each entry.
    tweetable_chunks = []
    # Iterate through the line and break it up into chunks. 
    chunks = [line[x:x + chunk_length] for x in range(0, line_length, chunk_length)]
    # However, we never want to append tweet_separator to the end of the last chunk
    # so we remove that chunk before looping through the preceding ones.
    last_chunk = chunks[-1]
    for chunk in chunks[:-1]:
        chunk = chunk + tweet_separator
        tweetable_chunks.append(chunk)
    # Add the last chunk to the list.
    tweetable_chunks.append(last_chunk)

    return tweetable_chunks

"""
Main script
"""
if __name__ == '__main__':
    # Open the data file and put the contents into an array
    # so we can grab the first line.
    with open(data_file_name) as f:
        lines = f.readlines()
        # If there is no data in the file, don't go any further.
        if not len(lines):
            exit 

    # Grab the first line.
    line = lines.pop(0)
    tweets = get_chunks(line.rstrip())

    # Now that we have removed the first line, save the remaining ones
    # back to the same file.
    output_file = open(data_file_name, 'w')
    for write_line in lines:
        output_file.write(write_line)

    # Send the tweet.
    twitter = Twitter(auth=OAuth(oa_access_token, oa_access_token_secret, consumer_key, consumer_secret))
    for tweet in tweets:
        twitter.statuses.update(status = tweet.strip())
