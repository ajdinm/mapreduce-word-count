from Trie import Trie

class Reducer:

    @staticmethod
    def reduce(t, t1): # adding t1 to t
        Reducer.helper(t.root, t1.root)

    @staticmethod
    def helper(node, node1):
        node.wordCount = node.wordCount + node1.wordCount
        for att in node1.arr:
            if att not in node.arr:
                node.arr.update({att: node1.arr[att]})
            else:
               Reducer.helper(node.arr[att], node1.arr[att])
        return 1
  
