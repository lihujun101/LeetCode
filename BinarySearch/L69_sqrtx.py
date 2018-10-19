class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_i = 0
        max_i = x
        if x == 1:
            return 1
        while max_i - min_i != 1:
            mid = int((min_i + max_i) / 2)
            if mid ** 2 > x:
                max_i = mid
            elif mid ** 2 < x:
                min_i = mid
            else:
                return mid
        return min_i


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(1))
