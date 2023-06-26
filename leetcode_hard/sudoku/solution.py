from functools import lru_cache
from typing import List


class Solution:
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        candidates = [str(i) for i in range(1, 10)]
        i = 0
        j = 0
        while i < 9 and j < 9:
            if board[i][j] == '.':
                for candidate in candidates:
                    board[i][j] = candidate
                    if self.isValid(board):
                        try:
                            self.solveSudoku(board)
                            return
                        except:
                            board[i][j] = '.'
                    else:
                        board[i][j] = '.'
                if board[i][j] == '.':
                    raise Exception()
            else:
                if i < 8:
                    i += 1
                else:
                    j += 1
                    i = 0

    # @lru_cache()
    def isValid(self, board: List[List[str]]) -> None:
        for i in range(9):
            row_seen = set()
            column_seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_seen:
                        return False
                    else:
                        row_seen.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in column_seen:
                        return False
                    else:
                        column_seen.add(board[j][i])      

        for i in range(9):
            row_offset = (i//3)*3
            column_offset = (i%3)*3
            square_seen = set()
            for j in range(3):
                for k in range(3):
                    char = board[row_offset + j][column_offset + k]
                    if char != '.':
                        if char in square_seen:
                            return False
                        else:
                            square_seen.add(char)
        return True



if __name__ == '__main__':
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    sol.solveSudoku(board)
    for row in board:
        print(row)


        