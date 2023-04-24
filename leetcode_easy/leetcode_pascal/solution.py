# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution():
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = list()
        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                last_row = result[i-1]
                new_row = list()
                new_row.append(1)
                for j in range(len(last_row)-1):
                    new_row.append(last_row[j] + last_row[j+1])
                new_row.append(1)
                result.append(new_row)
        return result