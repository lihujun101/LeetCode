class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                if max_value < count:
                    max_value = count
                count = 0
            elif nums[i] == 1:
                count += 1
        if max_value < count:
            max_value = count
        return max_value


if __name__ == '__main__':
    l = [1, 1, 0, 1, 1, 1]
    s = Solution()
    print(s.findMaxConsecutiveOnes(l))
