class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums_set = set()
        for i in nums2:
            if i in nums1_set:
                nums_set.add(i)
        return list(nums_set)
