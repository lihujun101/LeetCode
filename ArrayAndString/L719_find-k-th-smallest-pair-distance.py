class Solution:

    # 方法说明：
    # 1、先排序，那么最小的差值可以认为是min=0，最大的差值就是max =nums[-1] - nums[0]
    # 2、那么mid = (min+max) // 2 ，当差值<=mid的个数可以通过getCount方法统计计算出来，但是注意getCount方法不是两个for循环
    # 3、可以知道差值越大，则个数越多；那么count数目大于K的话，mid范围就是[left,mid],count数目小于k的话，则mid范围就是[mid+1,right]
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = self.getCount(nums, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    # 统计差值<=m的个数
    def getCount(self, nums, m):
        # nums是排序好的列表
        count = 0
        left_idx = 0

        # 注意这里没有使用双for循环，双for循环时间复杂度为O(n^2)
        for i in range(1, len(nums)):
            # 当num[i]- nums[left_idx] > m ，则left_idx向右移动
            while nums[i] - nums[left_idx] > m:
                left_idx += 1
            count += i - left_idx

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.getCount([1, 2, 3, 4, 5, 6, 7], 2))
