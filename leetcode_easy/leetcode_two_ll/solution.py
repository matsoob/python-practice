# https://leetcode.com/problems/intersection-of-two-linked-lists/
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_set = set()
        curr_a = headA
        while curr_a:
            a_set.add(curr_a)
            curr_a = curr_a.next
        curr_b = headB
        while curr_b:
            if curr_b in a_set:
                return curr_b
            curr_b = curr_b.next
        return None

    def getIntersectionNodeSpaceEfficient(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr_a = headB
        curr_b = headA
        while (curr_a is not curr_b):
            curr_a = curr_a.next if curr_a else headA
            curr_b = curr_b.next if curr_b else headB
        return curr_a