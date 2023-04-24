# https://leetcode.com/problems/valid-parentheses/
from collections import deque

class Solution:
    OPENERS = ["(", "[", "{"]
    PARENTHESES_PAIRS = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    def isValid_list(self, s: str) -> bool:
        opening_ps = []
        for char in s:
            if char in self.OPENERS:
                opening_ps.append(char)
            elif char in self.PARENTHESES_PAIRS:
                if len(opening_ps) == 0:
                    return False
                last_opener = opening_ps.pop()
                if last_opener != self.PARENTHESES_PAIRS[char]:
                    return False
        if len(opening_ps) > 0:
            return False
        return True

    def isValid_deque(self, s:str) -> bool:
        opening_ps = deque()
        for char in s:
            if char in self.OPENERS:
                opening_ps.append(char)
            elif char in self.PARENTHESES_PAIRS:
                if len(opening_ps) == 0:
                    return False
                last_opener = opening_ps.pop()
                if last_opener != self.PARENTHESES_PAIRS[char]:
                    return False
        if len(opening_ps) > 0:
            return False
        return True  
