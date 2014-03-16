import random
import cPickle as pickle
import tweepy

#Tweepy setup

keys = [line.rstrip('\n') for line in open('twitterkeys.txt')]

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_KEY = keys[2]
ACCESS_SECRET = keys[3]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


corpus = 'poe'
database = pickle.load(open(corpus+'.p'))

try:
    seed = pickle.load(open('lastseed.p'))
except IOError:
    seed = database.keys()[random.randint(0, len(database.keys())-1)]


def generate(words, seed):
    gentext = []

    while len(gentext) < int(words):
        gentext.append(seed[0])
        new = database[seed][random.randint(0, len(database[seed])-1)]
    
        seed = (seed[1], new)
        pickle.dump(seed, open('lastseed.p', 'w'))
    #return gentext

#def sentences(gentext):
    while True:
        if gentext[0].isupper():
            break
        else:
            gentext.pop(0)

    endpunct = ['.', '?', '!']
    sentence = []

    for word in gentext:
        if word[-1] not in endpunct:
            sentence.append(word)
        else:
            sentence.append(word)
            print " ".join(sentence)
            break

#sentences(generate(100, seed))
generate(100, seed)
