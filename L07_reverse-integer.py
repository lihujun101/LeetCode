class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            s = '-' + str(x)[1:][::-1]
        elif x > 0:
            s = str(x)[::-1]
        else:
            return 0
        if int(s) > -2**31 and int(s) < 2**31 - 1:
            return int(s)
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(121))
