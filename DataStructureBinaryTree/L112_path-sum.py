class Solution:

    # 递归条件：hasPath(self,root.left,sum-root.val)
    # 神答案啊，我实在想不到啊
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.right is None and root.left is None:
            return root.val == sum
        return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)