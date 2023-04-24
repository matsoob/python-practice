# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = dict()
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        for c in t:
            if c in chars:
                chars[c] -= 1
                if chars[c] < 0:
                    return False
            else:
                return False
        return True