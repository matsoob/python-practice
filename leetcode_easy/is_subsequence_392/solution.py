# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        for char in t:
            if s_pointer == len(s):
                return True
            if s[s_pointer] == char:
                s_pointer += 1

        return s_pointer == len(s)