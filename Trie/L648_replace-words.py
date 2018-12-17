class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node('_')

    def insert(self, root):
        cur = self.root
        for char in root:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.end = True

    def search(self, successor):
        cur = self.root
        count = 0
        for char in successor:
            if char not in cur.children or cur.end is True:
                break
            cur = cur.children[char]
            count += 1
        if cur.end is True:
            return successor[:count]
        else:
            return None



class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.insert(word)
        sentence_word = sentence.split(' ')
        new_words = []
        for every_word in sentence_word:
            if trie.search(every_word) is None:
                new_words.append(every_word)
            else:
                new_words.append(trie.search(every_word))
        return ' '.join(new_words)


if __name__ == '__main__':
    s = Solution()
    dict = ["cat", "bat", "rat",'a','aa','aaaa']
    sentense = "the cattle was rattled by the battery aaaaaaaa"
    print(s.replaceWords(dict, sentense))
