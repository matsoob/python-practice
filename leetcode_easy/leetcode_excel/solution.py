# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        current = 0
        for char in columnTitle:
            current = current * 26 + ord(char) - 64
        return current