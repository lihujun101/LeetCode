class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # 动态规划：
        # 1、起始和的字典             dp[0] = {0:1}
        # 2、第1个数+-1,此时和的字典为 dp[1] = {1:1,-1:1}
        # 3、第2个数+-1,此时和的字典为 dp[2] = {2:1,0:2,-2:1}
        # 4、第3个数+-1,此时和的字典为 dp[3] = {3:1,1:3,-1:3,-3:1},target为1时，那么返回dp[3][1],即3
        # 比如dp[3][1] = dp[2][2]+dp[2][0] = 1 + 2 = 3
        # 和字典的动态转义方程  dp[i][j] = dp[i-1][j-num] + dp[i-1][j+num]
        sums = 0
        for n in nums:
            sums += n
        sum_diff = sums - S
        if sum_diff < 0 or sum_diff % 2 != 0:
            return 0

        dp = {0: 1}
        for n in nums:
            temp = {}
            for sign in (1, -1):
                for j in dp:
                    key = j + n * sign
                    if key not in temp:
                        value = dp[j]
                    else:
                        value = temp[key] + dp[j]
                    temp[key] = value
            dp = temp
        return dp[S]


if __name__ == '__main__':
    s = Solution()
    a = s.findTargetSumWays([1,1,1,1,1], 3)
    print(a)
