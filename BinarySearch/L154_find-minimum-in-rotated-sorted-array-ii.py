class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums[0] < nums[-1]:
            return nums[0]
        if nums[0] > nums[-1]:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
            return nums[left]

        if nums[0] == nums[-1]:
            # left = 0
            # right = len(nums) - 1
            # while left <= right:
            #     if nums[left] == nums[right]:
            #         left += 1
            #         right -= 1
            #     else:
            #         return min(nums[-1],self.findMin(nums[left:right + 1]))
            # return nums[(left + right) // 2]
            pass


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([4, 3, 2, 1, 0]))
