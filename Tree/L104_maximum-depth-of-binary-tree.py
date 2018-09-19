from collections import deque


class TreeNode:
    def __init__(self, x,left=None,right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if left_depth > right_depth:
            return left_depth + 1
        elif right_depth >= left_depth:
            return right_depth + 1

