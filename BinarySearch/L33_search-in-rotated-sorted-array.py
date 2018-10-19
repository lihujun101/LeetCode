class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        if len(nums) == 0: return -1

        # 找到旋转位置，否则表示没有旋转
        if nums[0] > nums[end]:
            mid = int((start + end) / 2)
            while start < end:
                if nums[mid] > nums[len(nums) - 1]:
                    start = mid + 1
                elif nums[mid] < nums[len(nums) - 1]:
                    end = mid
                mid = int((start + end) / 2)
               
            if target >= nums[0] and target <= nums[mid - 1]:
                start_idx = 0
                end_idx = mid - 1
            elif target >= nums[mid] and target <= nums[len(nums) - 1]:
                start_idx = mid
                end_idx = len(nums) - 1
            else:  # 大于最大值，小于最小值，直接不可能存在
                return -1
        else:
            start_idx = 0
            end_idx = len(nums) - 1

        while True:
            mid_idx = int((start_idx + end_idx) / 2)

            if target > nums[mid_idx]:
                start_idx = mid_idx + 1

            elif target < nums[mid_idx]:
                end_idx = mid_idx

            else:
                return mid_idx

            if (mid_idx == start_idx and mid_idx == end_idx) or start_idx > end_idx:
                return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[3,2], target=2))
