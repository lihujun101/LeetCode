class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    # 中序遍历 ：左根右,判断是否为升序
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = self.in_tranverse(root)
        if not result:
            return True
        if len(result) == 0:
            return False
        if len(result) == 1:
            return True

        for i in range(len(result) - 1):
            first = result[i]
            second = result[i + 1]
            if first >= second:
                return False
        return True

    def in_tranverse(self, root):
        if root:
            self.in_tranverse(root.left,)

            self.result.append(root.val)
            self.in_tranverse(root.right)
        return self.result


if __name__ == '__main__':
    a1 = TreeNode(1)
    a2 = TreeNode(1)
    # a3 = TreeNode(3)
    # a4 = TreeNode(4)
    # a5 = TreeNode(4)
    a1.left = a2
    # a1.right = a3
    # a3.left = a4
    # a3.right = a5

    s = Solution()
    print(s.isValidBST(a1))
