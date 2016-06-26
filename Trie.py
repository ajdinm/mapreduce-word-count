from Node import Node
from graphviz import Digraph
import pickle

class Trie:

    def __init__(self):
        self.root = Node(dict())
        self.graph = Digraph(comment='My first trie')

    def addSymbol(self, char, node = None):
        if node is None:
            node = self.root
        if len(char) == 0:
            node.wordCount = node.wordCount + 1
            return
        try:
            self.addSymbol(char[1:], node.arr[char[0]])
        except KeyError:
            node.arr.update({char[0]: Node(dict())})
            self.addSymbol(char[1:], node.arr[char[0]])

    def dumpTrie(self, node = None):
        if node is None:
            node = self.root
        word=''
        if node.wordCount > 0:
            word = str(node.wordCount)
        self.graph.node(str(node), word)
            
        for key in node.arr:
            self.graph.edge(str(node), str(node.arr[key]), label=key)
            self.dumpTrie(node.arr[key])
    def showTrie(self, key):
        self.dumpTrie()
        self.graph.render(key, view=True)

    def getSource(self):
        self.dumpTrie()
        return self.graph.source;

    def printWords(self, node = None, path = '' ):
        if node is None:
            node = self.root
        if node.wordCount > 0:
            print '%s\t%s' % (path, node.wordCount)
        for key in node.arr:
            self.printWords(node.arr[key], path + key)
