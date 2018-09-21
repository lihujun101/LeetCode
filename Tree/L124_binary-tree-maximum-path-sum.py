class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
# 这道题最早做成了从叶子节点出发必须到另外一个叶子节点处，花了很多时间做。5555555555555555
class Solution:
    path_sum = []
    sum = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left is None and root.right is None:
            return root.val
        self._traverse(root)
        return max(self.path_sum)

    # 思路
    # 1、先找叶子节点，最底层开始，所有节点均化成left,root,right
    # 2、从叶子节点中，如left=1,val=2,right=3,计算结果为6
    # 3、计算后，将left,right置为None，然后val值为val+right
    # 4、依次内推再计算节点的值

    def _traverse(self, root):

        if root.left is not None and root.right is not None:
            self.sum += root.val + self._traverse(root.left) + self._traverse(root.right)
            self.path_sum.append(self.sum)
            self.sum = 0
            root.val = max(root.left.val, root.right.val) + root.val
            root.left, root.right = None, None
        elif root.left is not None and root.right is None:
            self.sum += root.val + self._traverse(root.left)
            self.path_sum.append(self.sum)
            self.sum = 0
            root.val = root.left.val + root.val

        elif root.right is not None and root.left is None:
            self.sum += root.val + self._traverse(root.right)
            self.path_sum.append(self.sum)
            self.sum = 0
            root.val = root.right.val + root.val
        return root.val

'''


class Solution:

    def maxPathSum(self, root):
        max = -float("inf")
        self.maxsum(root)
        return self.max

    def maxsum(self, root):
        if root is None:
            return
        sum = root.val
        lmax, rmax = 0, 0
        if root.left:
            lmax = self.maxsum(root.left)
            if lmax > 0:
                sum += lmax
        if root.right:
            rmax = self.maxsum(root.right)
            if rmax > 0:
                sum += rmax
        if sum > self.max:
            self.max = sum
        return max(root.val, max(root.val + lmax, root.val + rmax))


    # 方法不优，不知道为什么过不了leetcode，自测OK
    # def maxPathSum(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root.left is None and root.right is None:
    #         return root.val
    #     self._traverse(root)
    #     return max(self.path_sum)
    #
    # path_sum = []
    # def _traverse(self, root):
    #
    #     if root.left and root.right:
    #         # 左右节点的值取大
    #         max_value = max(self._traverse(root.left), self._traverse(root.right))
    #         # 左右节点+该节点的和
    #         sum_value = root.val + root.left.val + root.right.val
    #
    #     elif root.right is not None and root.left is None:
    #         max_value = self._traverse(root.right)
    #         sum_value = root.val + + root.right.val
    #     elif root.right is None and root.left is not None:
    #         max_value = self._traverse(root.left)
    #         sum_value = root.val + root.left.val
    #     else:
    #         return root.val
    #
    #     # 该节点和左右节点中任意一个大值的和
    #     value = root.val + max_value
    #     # 将max_value、sum_value、value中大值追加至path_sum
    #     self.path_sum.append(max(max_value, sum_value, value))
    #     # 该节点的值和左右节点的值大值相加，如果相加结果更大就替换掉
    #     root.val = max((root.val + max_value), root.val)
    #     return root.val


if __name__ == '__main__':
    root = TreeNode(-3)
    root.left = TreeNode(-2)
    root.left.left = TreeNode(-5)
    root.left.right = TreeNode(-4)
    root.right = TreeNode(-1)
    root.right.left = TreeNode(-6)
    root.right.right = TreeNode(-2)

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    s = Solution()
    s1 = s.maxPathSum(root)
    print(s1)
