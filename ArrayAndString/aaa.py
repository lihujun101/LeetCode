class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # 方法：
        # 1、起点在[0,0],路线是先右行
        # 2、遇到墙壁就是下行
        # 3、遇到墙壁就左行
        # 4、遇到墙壁就上行
        # 5、遇到墙壁后依次重复 1、2、3、4

        if len(matrix) == 0:
            return matrix
        if len(matrix) == 1:
            return matrix[0]

        # 墙壁的基准线
        up, left, down, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        i, j = 0, 0
        matrix_list = []
        while len(matrix_list) < len(matrix) * len(matrix[0]):
            # move to right
            while j <= right:
                # 这里处理up的原因是因为向上移动的时候会走到(0,0)这个位置，或者其他使用过的位置
                if up > i:
                    i += 1
                    j += 1
                matrix_list.append(matrix[i][j])
                if j < right:
                    j += 1
                if j == right:
                    break


            right -= 1

            # move to down
            while i <= down:
                matrix_list.append(matrix[i][j])
                if i < down:
                    i += 1
            down -= 1

            # move to left
            while j >= up:
                matrix_list.append(matrix[i][j])
                if j > up:
                    j -= 1

            up += 1

            # move to up
            while i >= left:
                matrix_list.append(matrix[i][j])
                if i > left:
                    i -= 1
            left += 1
        return matrix_list


if __name__ == '__main__':
    nums = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s = Solution()
    print(s.spiralOrder(nums))
