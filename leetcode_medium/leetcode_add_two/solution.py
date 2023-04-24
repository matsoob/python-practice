# https://leetcode.com/problems/add-two-numbers/description/
from typing import Optional
from linked_list.linked_list import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: convert to int do math
        total = 0
        current_pow = 1
        while l1:
            total += l1.val * current_pow
            current_pow *= 10
            l1 = l1.next
        current_pow = 1
        while l2:
            total += l2.val * current_pow
            current_pow *= 10
            l2 = l2.next
        temp = ListNode(None)
        curr = temp
        while True:
            curr.next = ListNode(total % 10)
            curr = curr.next
            total = total // 10
            if total == 0:
                break
        return temp.next
    
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: don't convert
        temp = ListNode(None)
        curr = temp
        carrying = False
        while l1 or l2:
            value = 0
            if l1:
                value += l1.val
            if l2:
                value += l2.val
            if carrying:
                value += 1
                carrying = False
            if value > 9:
                value = value % 10
                carrying = True
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carrying:
            curr.next = ListNode(1)
        return temp.next