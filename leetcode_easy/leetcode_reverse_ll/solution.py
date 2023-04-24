# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Reverse Values
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = list()
        current = head
        # Iterates through once, O(n)
        while current:
            stack.append(current)
            current = current.next
        current = head
        # Iterates through once/2, O(n)
        for i in range(len(stack)//2):
            pointer = len(stack) - i - 1
            temp = current.val
            current.val = stack[pointer].val
            stack[pointer].val = temp
            current = current.next
        # Space complexity is O(n)
        return head 

    # Reverse by pointers (so Nodes themselves are getting reversed)
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        last = None
        current = head
        # Time complexity O(n), Space complexity O(1)
        while current:
            temp = current.next
            current.next = last
            last = current
            current = temp
        return last
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        def repoint_things_after_me(me: ListNode) -> ListNode:
            if me.next:
                new_head = repoint_things_after_me(me.next)
                me.next.next = me
                return new_head
            else:
                return me
        new_head = repoint_things_after_me(head)
        head.next = None
        return new_head