class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        num = str(n)
        n_set = {num}
        while num != '1':
            length = len(num)
            i = 0
            sum = 0
            while i < length:
                sum += int(num[i]) ** 2
                i += 1
            if str(sum) not in n_set:
                n_set.add(str(num))
                num = str(sum)
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(11))
