# https://leetcode.com/problems/palindrome-partitioning/
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        grid = [[None]*n for _ in range(n)]
        for i in range(n):
            grid[i][i] = True
        for i in range(n-1):
            grid[i][i+1] = s[i] == s[i+1]
        for i in range(n):
            for j in range(i+2, n):
                prev_is_palin = grid[i+1][j-i]
                if prev_is_palin and s[i] == s[j]:
                    grid[i][j] = True
                else:
                    grid[i][j] = False
        # Now we have all the palindromes
        # I guess it might be a knapsack problem where we're trying all the ways to 
        # combine from the list of palindromes we now have??
        pass