class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count = self.getCount(nums, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def getCount(self, nums, mid):
        count = 0
        left_idx = 0
        for i in range(1, len(nums)):
            while (nums[i] - nums[left_idx]) > mid:
                left_idx += 1
            count = count + (i - left_idx)
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.smallestDistancePair(nums=[1, 3, 1], k=3))
