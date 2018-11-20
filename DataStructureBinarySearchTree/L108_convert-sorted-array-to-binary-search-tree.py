class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)

        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])
        if length == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        mid = int(length / 2)
        root = TreeNode(nums[mid])
        nums_left = nums[:mid]
        nums_right = nums[mid + 1:]
        root.left = self.sortedArrayToBST(nums_left)
        root.right = self.sortedArrayToBST(nums_right)
        return root
