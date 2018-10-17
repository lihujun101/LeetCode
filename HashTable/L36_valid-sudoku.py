class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m, n = 0, 0
        locations = []
        for i in range(9):
            # 横
            board_set = set()
            for ii in range(9):
                if board[i][ii] == '.':
                    continue
                if board[i][ii] not in board_set:
                    board_set.add(board[i][ii])
                else:
                    return False
            # 竖
            board_set = set()
            for ij in range(9):
                if board[ij][i] == '.':
                    continue
                if board[ij][i] not in board_set:
                    board_set.add(board[ij][i])
                else:
                    return False

            # 3X3小框
            board_set = set()
            for mi in range(m, m + 3):
                for ni in range(n, n + 3):
                    if board[mi][ni] == '.':
                        continue
                    if board[mi][ni] not in board_set:
                        board_set.add(board[mi][ni])
                    else:
                        return False

            if n == 6:
                m += 3
                n = 0
            else:
                n += 3
        return True


if __name__ == '__main__':
    boards = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    s = Solution()
    print(s.isValidSudoku(boards))
