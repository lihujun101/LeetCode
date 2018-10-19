class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        else:
            left = 0
            right = len(nums) -1
            last = nums[len(nums) -1]
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > last:
                    left = mid + 1
                elif nums[mid] < last:
                    right = mid
            return nums[right]


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([4,3,1]))
