class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 时间复杂度为O(n)的方法：需两次遍历
        # 1、如[1,2,3,4]，找到最大值,并将最大值替换成负无穷
        # 2、再次遍历，找到最大的值，此时就是次大的数~

        if len(nums) == 1:
            return 0
        max_value,  max_idx =  nums[0], 0
        min_value = -float('inf')
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_idx = i
                max_value = nums[i]
            if nums[i] < 0:
                return -1
        # 替换最大值
        nums[max_idx] = min_value
        second_value = nums[0]
        for i in range(len(nums)):
            if nums[i] > second_value:
                second_value = nums[i]

        if max_value > 0 and second_value == 0:
            return max_idx
        if max_value / second_value >= 2:
            return max_idx
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.dominantIndex(nums=[1,0]))
