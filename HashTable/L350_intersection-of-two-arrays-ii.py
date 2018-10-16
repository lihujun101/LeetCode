class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = {}
        nums2_dict = {}
        for num in nums1:
            if num not in nums1_dict:
                nums1_dict[num] = 1
            else:
                nums1_dict[num] += 1

        for num in nums2:
            if num in nums1_dict:
                if num not in nums2_dict:
                    nums2_dict[num] = 1
                else:
                    nums2_dict[num] += 1
        nums = []
        for num in nums2_dict:
            i = 0
            while i < min(nums2_dict[num],nums1_dict[num]):
                nums.append(num)
                i += 1

        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.intersect(nums1=[1], nums2=[]))
