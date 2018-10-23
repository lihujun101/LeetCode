class Solution:


    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_n = 1
        max_n = len(nums) - 1


        while min_n < max_n:
            mid = (min_n + max_n) // 2
            count_less = 0
            # count_eq = 0
            for num in nums:
                if num <= mid:
                    count_less += 1
            if count_less > mid:
                max_n = mid
            else:
                min_n = mid + 1

        return min_n


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([2,2,2,3,4,5,6,7]))
