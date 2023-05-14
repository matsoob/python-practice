
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen_column = set()
            seen_row = set()
            for j in range(9):
                fig_row = board[i][j]
                fig_column = board[j][i]
                if fig_row in seen_row:
                    return False
                else:
                    if fig_row != '.':
                        seen_row.add(fig_row)
                if fig_column in seen_column:
                    return False
                else:
                    if fig_column != '.':
                        seen_column.add(fig_column)
        for i in range(9):
            seen_square = set()
            row_offset = (i % 3) * 3
            col_offset = (i // 3) * 3
            for j in range(3):
                for k in range(3):
                    fig = board[j+row_offset][k+col_offset]
                    if fig in seen_square:
                        return False
                    if fig != '.':
                        seen_square.add(fig)
        return True