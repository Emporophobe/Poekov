Poekov
======

Twitter + Markov Chains + Poe

This program generates Tweets based on a selection of short stories by Edgar Allan Poe, and recombines words and phrases using Markov Chains.

Installation
============
Poekov requires Tweepy and a Twitter account with developer credentials to post to Twitter. Get Tweepy from https://github.com/tweepy/tweepy and install it first. Visit https://dev.twitter.com/ to set up your developer credentials and create a new application with both read and write permissions.

Download the repo to a single directory. You must also create a .txt file named "twitterkeys.txt" (without quotes) in which you put, one per line:

API key
API secret
Access Token
Access Token Secret

Modifications
==========
If you want to change the corpus (source text, determines the style of the output text), find a .txt file that contains your new corpus. Place it in the Poekov directory. Run markovgen3.py, and input the name of your text file when prompted. This will generate a pickle (.p) file that should be several times larger than the text file. Edit poekov.py, changing the variable 'corpus' from 'poe' to the name of your text file. 

The other main variable is the time between tweets, found as the argument of time.sleep(seconds). Changing this from the default of 3600 seconds (1 hour) will change the frequency of tweets. Keep in mind there is a limit to the number of tweets per day.
