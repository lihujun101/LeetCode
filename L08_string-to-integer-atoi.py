import re

class Solution:
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        nums = re.findall(r'^([-+]?\d+)', string.strip())
        if nums == []:
            return 0
        num = int(nums[0])
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return num
if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('+3'))
