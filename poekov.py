import random
import cPickle as pickle
import tweepy


corpus = 'poe'

database = pickle.load(open(corpus+'.p'))

seed = database.keys()[random.randint(0, len(database.keys())-1)]

stringlength = 500
gentext = []

while len(gentext) < stringlength:
    gentext.append(seed[0])
    new = database[seed][random.randint(0, len(database[seed])-1)]
    
    seed = (seed[1], new)

print " ".join(gentext)
