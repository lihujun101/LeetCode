# Definition for a Node.
class Node(object):
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class Solution(object):
    # 自上而下的做法
    ans = 0
    def maxDepth(self, root, depth=1):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        if root.children is None:
            self.ans = max(self.ans, depth)
        if root.children:
            children = root.children
            for child in children:
                self.maxDepth(child, depth + 1)
        return self.ans


if __name__ == '__main__':
    node1 = Node(1)
    node3 = Node(3)
    node2 = Node(2)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    children1 = [node3, node2, node4]
    node1.children = children1
    children2 = [node5, node6]
    node3.children = children2
    node8 = Node(8)
    node9 = Node(9)
    children3 = [node8]
    children4 = [node9]
    node4.children = children3
    node8.children = children4

    s = Solution()
    num = s.maxDepth(node1)
    print(num)
