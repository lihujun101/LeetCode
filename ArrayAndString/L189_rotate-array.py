class Solution:
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        k_new = k % len(nums)
        # 这种方法是O(n^2)
        for i in range(k_new):
            tmp = nums[len(nums) - 1]
            i = 0
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = tmp

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 时间复杂度O(n)
        k_new = k % len(nums)
        pass


if __name__ == '__main__':
    l = [1]
    s = Solution()
    s.rotate1(l, 2)
    print(l)
