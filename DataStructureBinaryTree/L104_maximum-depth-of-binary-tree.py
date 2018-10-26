class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    anwser = 0

    def maxDepth(self, root, depth = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 自顶向下的递归
        if root is None:  # 递归出口
            return 0
        self.anwser = max(self.anwser, depth)
        self.maxDepth(root.left, depth + 1)
        self.maxDepth(root.right, depth + 1)
        return self.anwser + 1


if __name__ == '__main__':
    a0 = TreeNode(0)
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)

    a0.left = a1
    a0.right = a2
    a1.left = a3
    a1.right = a4
    a4.right = a5
    s = Solution()

    print(s.maxDepth(a0))
