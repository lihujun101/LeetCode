class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法：
# 1、递归搜索，左右高度比较
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if abs(self._height(root.left) - self._height(root.right)) > 1:
            return False
        else:# Ture and False；这里不仅比较了根节点也比较了其他节点
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def _height(self, root):
        if root is None:
            return 0
        return max(self._height(root.left), self._height(root.right)) + 1


if __name__ == '__main__':
    node = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node.left = node1
    node.left.left = node2
    s = Solution()
    m = s.isBalanced(node)
    print(m)
