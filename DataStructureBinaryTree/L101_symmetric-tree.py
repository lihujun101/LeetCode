class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 方法：
    # 1、左子树的根节点的值 == 右子树根节点的值
    # 2、然后向下走一个节点 左子树的右子树的值 == 右子树的左子树的值，左子树的左子树的值 ==右子树的右子树 的值
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isMirror(root,root)

    def _isMirror(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            if self._isMirror(left.left,right.right) and self._isMirror(left.right,right.left):
                return True
        return False




if __name__ == '__main__':
    a0 = TreeNode(1)
    a1 = TreeNode(2)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(3)
    #a5 = TreeNode(5)

    a0.left = a1
    a0.right = a2
    a1.right = a3
    a2.right = a4
#
    s = Solution()

    print(s.isSymmetric(a4))