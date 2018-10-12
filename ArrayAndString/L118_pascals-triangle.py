class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        # 先建立一个空的二维列表
        nums_list = []
        for i in range(numRows):
            nums = [None] * (i + 1)
            nums_list.append(nums)

        nums_list[0] = [1]
        line = 1
        while line <= numRows - 1:
            nums_list[line][0] = 1
            nums_list[line][line] = 1
            i = 1
            while i < line:
                nums_list[line][i] = nums_list[line - 1][i - 1] + nums_list[line - 1][i]
                i += 1
            line += 1

        return nums_list


if __name__ == '__main__':
    s = Solution()
    print(s.generate(8))
