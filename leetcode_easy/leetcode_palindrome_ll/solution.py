# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional
from linked_list.linked_list import ListNode


class Solution:
    def isPalindromeSimple(self, head: Optional[ListNode]) -> bool:
        current = head
        vals = list()
        while current:
            vals.append(current.val)
            current = current.next
        for i in range(len(vals)//2):
            if vals[i] != vals[-1-i]:
                return False
        return True
        # O_n time, O_n space complexity

    def isPalindromeSmall(self, head: Optional[ListNode]) -> bool:
        # This seems to involve manipulating the original LL (into an invalid LL), which I'm not a fan of
        pass
