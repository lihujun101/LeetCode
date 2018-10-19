def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left != right:
            mid = (left + right) // 2
            if isBadVersion(mid) is False:
                left = mid + 1
            else:
                right = mid
        if isBadVersion(left - 1) is False and isBadVersion(left) is True:
            return left
        else:
            return -1
