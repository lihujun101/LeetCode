# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        # 不能这样写，children是个Node的列表[Node1,Node2]
        # depth = self.maxDepth(root.children)
        if not root.children:
            return 1
        return max(list(map(self.maxDepth,root.children))) + 1


if __name__ == '__main__':
    node = Node(1, None)
    s = Solution()
    print(s.maxDepth(node))
