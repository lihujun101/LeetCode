class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 0
        while n ** 2 < num:
            n += 1
        return n ** 2 == num


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(9))
