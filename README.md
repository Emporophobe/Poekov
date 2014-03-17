Poekov
======

Twitter + Markov Chains + Poe = @Poekov

This program uses Markov Chains to create unique tweets based upon a selection of short stories by Edgar Allan Poe.

https://twitter.com/Poekov

Installation
============
Poekov requires Tweepy and a Twitter account with developer credentials to post to Twitter. Get Tweepy from https://github.com/tweepy/tweepy and install it first. Visit https://dev.twitter.com/ to set up your developer credentials and create a new application with both read and write permissions.

Download the repo to a single directory. You must also create a .txt file named "twitterkeys.txt" (without quotes) in which you put, one per line:

  API key, 
  API secret, 
  Access Token, 
  Access Token Secret

This should only contain the keys, without punctuation etc.

Alterations
==========
If you want to change the corpus (source text, determines the style of the output text), find a .txt file that contains your new corpus. Place it in the Poekov directory. Run markovgen3.py, and input the name of your text file when prompted. This will generate a pickle (.p) file that should be several times larger than the text file. This may take several minutes to complete. Edit poekov.py, changing the variable 'corpus' from 'poe' to the name of your text file. 

The other main variable is the time between tweets, found as the argument of time.sleep(seconds). Changing this from the default of 3600 seconds (1 hour) will change the frequency of tweets. Keep in mind there is a limit to the number of tweets per day.

Sources
=======
"The Black Cat", 
"The Cask of Amontillado", 
"A Descent into the Maelstrom", 
"The Facts About the Case of M. Valdemar", 
"The Fall of the House of Usher", 
"The Gold-Bug", 
"The Imp of the Perverse", 
"The Masque of the Red Death", 
"The Murders in the Rue Morgue", 
"The Oval Portrait", 
"The Pit and the Pendulum", 
"The Premature Burial", 
"The Purloined Letter", 
"The Tell-Tale Heart".
