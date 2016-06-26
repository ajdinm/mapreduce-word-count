#!/usr/bin/env python

from operator import itemgetter
import sys
import pickle

from Reducer import Reducer
from Trie import Trie
import sys

current_key = None
current_trie = Trie()
key = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, filename = line.split('\t', 1)
    file = open(filename, mode = 'rb')
    t = pickle.load(file)
    if current_key == key:
        # join tries
        Reducer.reduce(current_trie, t)
    else:
        if current_key:
            #traverse tries
            current_trie.printWords(path = current_key)
        current_trie = t
        current_key = key
if current_key == key:
    current_trie.printWords(path = current_key)








