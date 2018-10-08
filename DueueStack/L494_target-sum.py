class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        # 1、先全部相加得到和sum0
        # 2、差sum_diff,找到任意N个数相加等于sum_diff的组合数
        sum0 = 0
        for num in nums:
            sum0 += num
        sum_diff = (sum0 - S) / 2
        if sum_diff == 0:
            return 1
