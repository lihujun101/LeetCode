class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i < j:
            mid = (i + j) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                j = mid
            else:
                i = mid + 1
        return i


def guess(n):
    pass
