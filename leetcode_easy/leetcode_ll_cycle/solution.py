# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow and fast:
            if slow is fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next if fast.next else None
        return False