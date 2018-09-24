class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_less, nums_0, nums_greater = [], [], []
        for i in nums:
            if i < 0:
                nums_less.append(i)
            elif i == 0:
                nums_0.append(i)
            else:
                nums_greater.append(i)
        # 假设正数的值相对少


