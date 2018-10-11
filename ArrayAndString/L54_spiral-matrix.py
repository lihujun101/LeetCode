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

        # 墙壁初始的基准线
        up, left, down, right = -1, -1, len(matrix), len(matrix[0])
        i, j = 0, 0
        matrix_list = []

        while True:
            while j < right:
                matrix_list.append(matrix[i][j])
                j += 1
            # j-1是因为多取到的一个值
            j -= 1
            # 向右边走完了，那当前走的这条线就是up墙，那下一步就要向下走了，那这是i+1
            up = i
            i += 1
            if len(matrix_list) >= len(matrix) * len(matrix[0]):
                break

            while i < down:
                matrix_list.append(matrix[i][j])
                i += 1
            i -= 1
            # 向下边走完了，那当前走的这条线就是right墙
            right = j
            j -= 1
            if len(matrix_list) >= len(matrix) * len(matrix[0]):
                break

            while j > left:
                matrix_list.append(matrix[i][j])
                j -= 1
            j += 1
            # 向左边走完了，那当前走的这条线就是down墙
            down = i
            i -= 1
            if len(matrix_list) >= len(matrix) * len(matrix[0]):
                break

            while i > up:
                matrix_list.append(matrix[i][j])
                i -= 1
            i += 1
            # 向上边走完了，那当前走的这条线就是left墙
            left = j
            j += 1
            if len(matrix_list) >= len(matrix) * len(matrix[0]):
                break

        return matrix_list


if __name__ == '__main__':
    nums = [[1, 2, 3],
            [5, 6, 7],
            [9, 10, 11]]
    s = Solution()
    print(s.spiralOrder(nums))
