
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # 其实有点类似于DP，因为一边计算一边找边缘位置，如果用深度搜索时间肯定没有这样快
        # 1、生成一个均为0的矩阵copy_matrix
        # 2、找到边缘1的位置matrix[i][j] = 0,并将copy_matrix[i][j]= num+1 初始情况下num = 0,并记录下当前的边缘位置
        # 3、边缘位置出现找边缘1 matrix[i][j]= 0 ,并将copy_matrix[i][j]= num+1 初始情况下,更新新的边缘位置
        # 4、当边缘位置没有的时候就结束


        copy_matrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        edge = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i > 0 and matrix[i - 1][j] == 1 and (i - 1, j) not in edge:
                        edge.add((i - 1, j))
                    if i < len(matrix) - 1 and matrix[i + 1][j] == 1 and (i + 1, j) not in edge:
                        edge.add((i + 1, j))
                    if j < len(matrix[0]) - 1 and matrix[i][j + 1] == 1 and (i, j + 1) not in edge:
                        edge.add((i, j + 1))
                    if j > 0 and matrix[i][j - 1] == 1 and (i, j - 1) not in edge:
                        edge.add((i, j - 1))
        num = 1
        while edge:
            temp = set()
            for i, j in edge:
                matrix[i][j] = 0
                copy_matrix[i][j] = num
            while edge:
                i, j = edge.pop()
                if i > 0 and matrix[i - 1][j] == 1 and (i - 1, j) not in temp:
                    temp.add((i - 1, j))
                if i < len(matrix) - 1 and matrix[i + 1][j] == 1 and (i + 1, j) not in temp:
                    temp.add((i + 1, j))
                if j < len(matrix[0]) - 1 and matrix[i][j + 1] == 1 and (i, j + 1) not in temp:
                    temp.add((i, j + 1))
                if j > 0 and matrix[i][j - 1] == 1 and (i, j - 1) not in temp:
                    temp.add((i, j - 1))
            edge = temp
            num += 1

        return copy_matrix


if __name__ == '__main__':
    s = Solution()
    s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 1, 1]])
