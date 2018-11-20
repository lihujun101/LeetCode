class Solution:
    # 对于题目的理解：
    # 1、nums [i] 和 nums [j] 的差的绝对值 <=t
    # 2、abs(i-j) = k

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # 来捋一捋这道题
        # 1、如果t = 0,那么说明nums中需要存在重复数
        # 2、如果t != 0 ，那么说明只要nums[i]- a中任意一个数 <=t 都满足条件
        # 3、这个a长度一定，一边add、一边remove
        lenth = len(nums)
        a = set()
        for i in range(lenth):
            if t == 0:
                if nums[i] in a:
                    return True
            else:
                for atem in a:
                    if abs(nums[i] - atem) <= t:
                        return True
            a.add(nums[i])
            if len(a) == k + 1:
                a.remove(nums[i - k])
        return False


if __name__ == '__main__':
    s = Solution()
    m = s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
    print(m)
