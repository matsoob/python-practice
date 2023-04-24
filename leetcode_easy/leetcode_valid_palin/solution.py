# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        chars = [ c for c in lower if c.isalnum()]
        length = len(chars)
        for i in range(length // 2):
            if chars[i] != chars[length-i-1]:
                return False
        return True