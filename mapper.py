#!/usr/bin/env python

from Trie import Trie
import pickle
import random
import string

import sys

t = Trie()
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        t.addSymbol(word)
for key in t.root.arr:
    temp = Trie()
    temp.root = t.root.arr[key]
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
    name = '/tmp/' + name
    file = open(name, 'wb')
    pickle.dump(temp, file)
    file.close()
    print '%s\t%s' % (key, name)
