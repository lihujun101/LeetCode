class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.father = None
        self.end = False


class WordDictionary:
    # 这道题显然需要知道每个层级的字母有哪些
    # 1、从尾部找，找到头部，因为每个node的父节点是一定的
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('root')
        self.levels = {}
        self.maxlevel = 0

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        level = 0
        for char in word:
            level += 1
            if char not in cur.children:
                cur.children[char] = Node(char)
                father = cur
                cur = cur.children[char]
                cur.father = father
                # 知道每个层级的node
                if level not in self.levels:
                    # 得到最大的level层级
                    if level > self.maxlevel:
                        self.maxlevel = level
                    self.levels[level] = {cur}
                else:
                    self.levels[level].add(cur)
            else:
                cur = cur.children[char]
        cur.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # 搜索的时候倒数就行了
        length = len(word)

        # 1、首先判断字符串的长度，长度大于level最大层级，则直接返回False
        if length > self.maxlevel:
            return False
        # 2、判断是否有该长度的字符串，如果没有这个长度的字符串，直接返回False；
        else:
            nodes = self.levels[length]
            new_nodes = set()
            for node in nodes:
                if word[length-1] != '.':
                    if node.end is True and node.val == word[length-1]:
                        new_nodes.add(node)
                else:
                    if node.end is True:
                        new_nodes.add(node)
            if new_nodes == set():
                return False
            else:
                reversed_word = word[::-1]
                while new_nodes:
                    node = new_nodes.pop()
                    for char in reversed_word:
                        if char == node.val or char== '.':
                            node = node.father
                    if node.val == 'root':
                        return True
                return False

if __name__ == '__main__':
    s = WordDictionary()
    s.addWord('bad')
    s.addWord('bed')
    a = s.search('.m.')
    print(a)