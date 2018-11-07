class Solution:
    # 我不知道这道题是不是这样考虑的，我采用2个指针
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        i = 0
        j = k + i
        length = len(nums)
        while j < length:
            if abs(nums[i] - nums[j]) == t:
                return True
            else:
                i += 1
                j += 1
        return False

if __name__ == '__main__':
    s= Solution()
    m = s.containsNearbyAlmostDuplicate([1,0,1,1],1,2)
    print(m)