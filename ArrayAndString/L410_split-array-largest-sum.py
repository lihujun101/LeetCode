class Solution(object):

    # 二分法
    # 方法：
    # 1、首先要知道不管怎么分，结果值的范围是多少
    # 2.1、nums = [7, 2, 5, 10, 8]的话，m = 3，如果nums中每个数都被分开的话就是[7] [2] [5] [10] [8]，那么它的结果就是10
    # 2.2、如果nums整个被分成一个数组的话，则[7, 2, 5, 10, 8]，他的结果就是32
    # 3、那么不管怎么分割，他的和一定是在10~32之间的,mid=21
    # 4、mid = 21 的时候，我们去分割，看下能分割成几组数据 [7,2,5] [10,8]，分割成2组了,<=目标组数3，那么需要将和的值变得更小才行，才有更多的分组，那么这个时候，我们的和的区间就应该是10~21
    # 5、mid = (10+20)//2 = 15 ，我们用和为15去分割，分割成[7,2,5] [10] [8] 分割成3组了, <= 目标组数3，那么需要将和的值更小才行，才有更多的分组，那么这个时候，我们的和区间就是10~15
    # 6、mid = 12 ,分割成[7,2][5][10][8]，有4组数据, >目标组数3,说明mid需要变大,取值应该在13~15之间
    # 7、mid = 14, 分割成[7,2,5][10][8]  有3组数据, <=目标组数3,说明mid需要变小,取值在 13~14
    # 8、mid = 13 ,分割成[7,2][5][10][8]， 有4组数据, >目标组数3,说明mid需要变大,取值应该在14~14之间
    # 9、left就是和
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.getCount(nums, mid) > m:
                left = mid +1
            else:
                right = mid
        return left

    # 计算目标和为target的时候能分为几组
    @staticmethod
    def getCount(nums, target):
        count = 0
        sum = 0
        for num in nums:
            sum += num
            if sum > target:
                count += 1
                sum = num
        count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7, 2, 5, 10, 8], 2))
