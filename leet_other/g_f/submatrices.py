
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    rows[i][j] = 0
                else:
                    if i > 0:
                        rows[i][j] = rows[i-1][j] + 1
                    else:
                        rows[i][j] = 1
        columns = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    columns[i][j] = 0
                else:
                    if j > 0:
                        columns[i][j] = columns[i][j-1] + 1
                    else:
                        columns[i][j] = 1


sol = Solution()
test =  [[1,0,1],[1,1,0],[1,1,0]]
print(sol.numSubmat(test))