class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        traverse_list = [(0, 0)]
        max_i = len(matrix)
        max_j = len(matrix[0])
        finded = {(0, 0)}
        while len(finded) == max_i * max_j:
            i, j = traverse_list[-1]
