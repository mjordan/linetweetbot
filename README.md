# Overview

Line Tweetbot reads data from a file, one line at a time, and tweets the data. If the line is longer than Twitter's limit of 140 characters, it splits the line up into smaller chunks and tweets all chunks in succession. It adds elipses ([...]) to the end of incomplete tweets but doesn't attempt to split long lines on word boundaries.

After a line from the data file is tweeted, it is removed from the file. This means that unless you add lines to the file over time, Line Tweetbot will eventually tweet every line in the file.

## General prerequisites

* A Twitter acccount for Line Tweetbot to tweet to.
* A data file.
* Python (and in some cases Perl).

## Python prerequisites

Line Tweetbot is written in Python. It uses the PTT ([Python Twitter Tools](http://mike.verdone.ca/twitter/) library, so you will need to make sure it is installed. Instructions are provided on the PTT website.

## Perl requirements

Line Tweetbot includes a simple Perl script, sentences2lines.pl, that converts a narrative text into a Line Tweetbot data file containing one sentence per line. You only need to use it (or worry about Perl requirements) if you want to split a narrative text like a Project Gutenberg book into one sentence per line so you can tweet the sentences. 

sentences2lines.pl uses the [Lingua::Sentence module](http://search.cpan.org/~achimru/Lingua-Sentence-1.00/lib/Lingua/Sentence.pm) which you will need to install, and the File::Slurp module, both of which install via cpan easily.

## Configuring your Twitter account so it can use Line Tweetbot as an app

Before Line Tweetbot can send tweets to an account, you will need to obtain the required API keys and authorize Line Tweetbot as an app in the account.

1. Log into https://dev.twitter.com/apps using the Twitter credientials for the account you want Line Tweetbot to tweet to.
2. Create a new app. It doesn't matter what you call it but it probably should have a relatively descriptive title.
3. Fill in the required fields under the Settings tab. In the Application Type section, the only setting you need to change is the application type -- make sure it is set to 'Read and Write'.
3. Generate OAuth keys.

It can take a little while for all the settings for your new app to become registered with Twitter.

The final step is to approve your app to access your Twitter account.

1. In your account's Settings options, choose Apps.
2. Your application should appear in the list of approved apps. If it doesn't, wait a while and check again. Generating API keys in the previous step should make the app appear automatically but as stated above, it can take a few minutes for the app settings to register with Twitter.

## Running Line Tweetbot

Once you have your Twitter consumer and OAuth API keys, add them to the "Config variables" section in line_tweetbot.py. You will also need to indicate the filename or path of your input file.

Sending tweets from your data file is as simple as running the line_tweetbot.py script manually, from a cronjob, etc.

## License

Public domain. See LICENSE file for details.

## Development

Improvements and bug fixes are welcome.

1. [Fork the repository](https://help.github.com/articles/fork-a-repo)
2. Fix a bug, add an improvement (maybe something like splitting long lines on word boundaries....). 
3. [Submit a pull request](https://help.github.com/articles/creating-a-pull-request) explaining what your code does.

