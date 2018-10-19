class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
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
    print(s.search([0,1],1))