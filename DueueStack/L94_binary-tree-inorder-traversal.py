class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 未使用递归的做法，递归会比较简单
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        result = []
        while stack:
            sub = stack.pop()
            if sub:
                if sub.left or sub.right:
                    stack += [sub.right, sub, sub.left]
                    sub.left = None
                    sub.right = None
                else:
                    result.append(sub.val)
            else:
                continue
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
    s.inorderTraversal(a0)
