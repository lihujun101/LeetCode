class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 写的比较丑~~，但是不重要了
        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        mid0 = -1
        while left + 1 < right:

            mid = (left + right) // 2
            if nums[mid] == target:
                mid0 = mid
                break
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            mid0 = left
        elif nums[right] == target:
            mid0 = right

        if mid0 == -1:
            return [-1, -1]
        else:
            left_i, right_i = 0, mid0
            while left_i + 1 < right_i:
                mid_i = (left_i + right_i) // 2
                if nums[mid_i] < nums[mid0]:
                    left_i = mid_i
                else:
                    right_i = mid_i
            if nums[left_i] == target:
                right_i = left_i



            left_j, right_j = mid0, len(nums) - 1
            while left_j + 1 < right_j:
                if nums[right_j] == nums[mid0]:
                    left_j = len(nums) - 1
                    break
                mid_j = (left_j + right_j) // 2
                if nums[mid_j] > nums[mid0]:
                    right_j = mid_j
                else:
                    left_j = mid_j
            if nums[right_j] == target:
                left_j = right_j
            return [right_i, left_j]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums=[1,1], target=1))
