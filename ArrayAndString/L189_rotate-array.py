class Solution:
    # def rotate1(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     if len(nums) == 0:
    #         return nums
    #     k_new = k % len(nums)
    #     # 这种方法是O(n^2)
    #     for i in range(k_new):
    #         tmp = nums[len(nums) - 1]
    #         i = 0
    #         for i in range(len(nums) - 1, 0, -1):
    #             nums[i] = nums[i - 1]
    #         nums[0] = tmp

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 时间复杂度O(n)
        k_new = k % len(nums)
        if k_new == 0:
            return
        last_idx = len(nums) - 1
        total = len(nums)
        n = 0
        idx = last_idx
        temp = nums[last_idx]
        while True:
            idx_0 = idx - k_new
            if idx_0 < 0:
                idx_0 += len(nums)
                if idx_0 == last_idx:
                    nums[idx] = temp
                    n += 1
                    if n < total:
                        last_idx = last_idx - 1
                        idx = last_idx
                        temp = nums[last_idx]
                        continue
                    else:
                        break
            nums[idx] = nums[idx_0]
            idx = idx_0
            n += 1
        return nums


if __name__ == '__main__':
    l = [1]  # [1, 2, 3, 4, 5, 6,7]
    s = Solution()
    s.rotate(l, 0)
    print(l)
