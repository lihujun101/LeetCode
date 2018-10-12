class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_1 = self._quicksort(nums)
        sum = 0
        for i in range(0,len(nums_1), 2):
            sum += nums_1[i]
        return sum

    def _quicksort(self, nums):
        if len(nums) < 2:
            return nums
        pivot = nums[0]
        less, greater ,mine = [], [] ,[]
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                mine.append(i)

        return self._quicksort(less) + mine + self._quicksort(greater)


if __name__ == '__main__':
    l = [1,2,3,2]
    s = Solution()
    print(s.arrayPairSum(l))
