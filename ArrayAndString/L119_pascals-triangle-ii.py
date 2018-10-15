from copy import deepcopy


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        row_1 = [1, 1]
        row_2 = [1, 1]
        count = 1
        while count < rowIndex:
            for i in range(len(row_2)):
                if i == 0 :
                    row_2[i] = 1
                else:
                    row_2[i] = row_1[i - 1] + row_1[i]
            count += 1
            row_2.append(1)
            row_1 = deepcopy(row_2)
        return row_2


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(4))
