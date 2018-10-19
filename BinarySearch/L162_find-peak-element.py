class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-float("inf"))
        left = 0
        right = len(nums)
        while left != right:
            mid = (left + right) // 2
            if mid + 1 > len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                elif nums[mid] > nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] < nums[mid - 1]:
                    right = mid
            else:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    left = mid + 1
                elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    right = mid
                else:
                    right = mid
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement(nums=[2,1,2]))
