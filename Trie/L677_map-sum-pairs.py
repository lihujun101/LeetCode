class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.num = 0
        self.end = False


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('root')

    def insert(self, word, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        cur = self.root
        if self._search(word):
            for char in word:
                cur.children[char].num = val
                cur = cur.children[char]
        else:
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Node(char)
                cur.children[char].num += val
                cur = cur.children[char]
        cur.end = True


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.num

    def _search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        if cur.end is True:
            return True
        else:
            return False

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

if __name__ == '__main__':
    s = MapSum()

    s.insert("a", 2)
    s.insert('apple',3)
