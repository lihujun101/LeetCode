class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        dp = [0] * (target + 1)
        dp[0] = 1
        for n in nums:
            i = target
            while (i >= n):
                dp[i] = dp[i] + dp[i - n]
                i = i - 1
        return dp[target]
if __name__ == '__main__':
    s = Solution()
    a1 =s.findTargetSumWays([1,1,2,3,4,5],5)
    print(a1)