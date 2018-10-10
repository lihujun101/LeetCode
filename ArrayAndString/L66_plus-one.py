class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for i in digits:
            num = num + str(i)
        num = int(num)
        num += 1
        num = str(num)
        num_list = []

        for i in num:
            num_list.append(int(i))
        return num_list


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9,9]))