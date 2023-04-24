# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        chars = dict()
        # O_n time, O_n space, go through once
        for i in range(len(s)):
            char = s[i]
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        # O_n time again
        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i
        # While the two for-loops are ugly, they still add up to O_n time
        return -1

