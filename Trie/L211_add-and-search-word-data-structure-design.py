class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('_')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
