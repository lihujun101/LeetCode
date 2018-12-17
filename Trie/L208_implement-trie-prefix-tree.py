class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('root')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node(char)  # children['a']= Node('a')
            cur = cur.children[char]
        # 最后一个字符特殊处理表示有这个以这个字符结尾的字符串存在
        cur.end = True

    def search(self, word):
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

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    s = Trie()
    s.insert('apple')
    result = s.search('appl')
    print(result)
