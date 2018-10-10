class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = -1
        if not nums:
            return -1
        sum_left = 0
        sum_right = 0
        for i in range(1, len(nums)):
            sum_right += nums[i]

        if sum_left == sum_right:
            return 0
        for i in range(1, len(nums)):
            sum_left += nums[i - 1]
            sum_right -= nums[i]
            if sum_left == sum_right:
                idx = i
                break
        return idx


if __name__ == '__main__':
    nums = []
    s = Solution()
    print(s.pivotIndex(nums))
