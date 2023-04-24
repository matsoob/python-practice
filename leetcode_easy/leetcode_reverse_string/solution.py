# https://leetcode.com/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        You must do this by modifying the input array in-place with O(1) extra memory.
        """
        for i in range(len(s)//2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
