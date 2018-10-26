# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root, level=0, result=None):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 自顶向下计算
        # 这道理看格式就应该知道使用的先序遍历：根、左子树、右子树;在处理的时候带上栈的层数
        if result is None:
            result = []
        if root:
            if level > len(result) - 1:
                result.append([])
            result[level].append(root.val)
            self.levelOrder(root.left, level=level + 1, result=result)
            self.levelOrder(root.right, level=level + 1, result=result)
        return result


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

    print(s.levelOrder(a0))
