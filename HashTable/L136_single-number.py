class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set()
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
            else:
                nums_set.remove(i)
        for i in nums_set:
            return i