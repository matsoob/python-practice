# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        OPEN = '('
        CLOSE = ')'
        result = list()
        result.append(([OPEN], 1, 1))
        
        for _ in range(n*2 - 1):
            temp = list()
            for curr, open_count, total_opens in result:
                if open_count == 0:
                    temp.append(([*curr, OPEN], 1, total_opens+1))
                else:
                    if total_opens < n:
                        temp.append(([*curr, OPEN], open_count+1, total_opens+1))
                    temp.append(([*curr, CLOSE], open_count-1, total_opens))
            result = temp
        return [''.join(pars) for pars, _, _ in result]
    
    def generateParenthesisBackTrack(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans