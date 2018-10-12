class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # O(n)的方法：
        # 1、sum和s对比，sum滚动计算，向右加，向左减
        if len(nums) == 0:
            return 0
        i, j = 0, 0
        sum, count, min_count = 0, 0, float("inf")
        while True:
            if sum < s:
                if j == len(nums):
                    break
                sum += nums[j]
                j += 1

            elif sum >= s:
                count = j - i
                if min_count > count:
                    min_count = count
                sum -= nums[i]
                i += 1

        return 0 if min_count == float("inf") else min_count


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(s=11, nums=[1,2,3,4,5]))
