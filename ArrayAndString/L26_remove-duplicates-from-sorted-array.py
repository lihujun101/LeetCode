class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums) - 1:
            temp = nums[i]
            i += 1
            if nums[i] == temp:
                del nums[i]
                i -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,2,2,3, 3]
    s.removeDuplicates(nums)
    print(nums)
