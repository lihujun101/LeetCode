class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 需找到每次开始的位置和结束的位置
        # 1、从开始节点开始start_location,并找到下一个start_location,从start->end,然后打印(i+1,j-1)，
        # 2、直至到end_location,并找到下一个end_location，从end出发至start,然后打印(i-1,j+1)
        # 3、循环1、2直至完成所有数据
        if len(matrix) == 0:
            return matrix
        if len(matrix) == 1:
            return matrix[0]

        start_i, start_j = 0, 0
        end_i, end_j = 1, 0
        i, j = 0, 0
        max_i, max_j = len(matrix) - 1, len(matrix[0]) - 1
        matrix_list = []

        while len(matrix_list) < (max_i + 1) * (max_j + 1):
            if (i, j) == (start_i, start_j):
                matrix_list.append(matrix[i][j])
                if start_j < max_j:
                    start_j += 1
                elif start_j == max_j:
                    start_i += 1
                i, j = start_i, start_j

                if i > max_i or j > max_j:
                    break
                while i < max_i and j > 0:
                    matrix_list.append(matrix[i][j])
                    i += 1
                    j -= 1
                end_i, end_j = i, j

            if (i, j) == (end_i, end_j):
                matrix_list.append(matrix[i][j])
                if end_i < max_i:
                    end_i += 1
                elif end_i == max_i:
                    end_j += 1
                i, j = end_i, end_j
                if i > max_i or j > max_j:
                    break
                while j < max_j and i > 0:
                    matrix_list.append(matrix[i][j])
                    i -= 1
                    j += 1
                start_i, start_j = i, j

        return matrix_list


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # [[1,2],[4,5],[7,8]]  #
    s = Solution()
    print(s.findDiagonalOrder(matrix))
