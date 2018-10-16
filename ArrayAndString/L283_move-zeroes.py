class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while i <= len(nums) - 1:
            if nums[i] == 0:
                del nums[i]
                count += 1
            else:
                i += 1
        for i in range(count):
            nums.append(0)



if __name__ == '__main__':
    nums = [0,0,1]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)
