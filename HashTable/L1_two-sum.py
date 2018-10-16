class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, k in enumerate(nums):
            if target - k in hash_map:
                return [hash_map[target-k],i]
            hash_map[k] = i



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums=[2, 7,2, 2, 2], target=4))
