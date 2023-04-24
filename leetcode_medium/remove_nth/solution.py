# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional
from linked_list.linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_head = ListNode(None, head)
        current = temp_head
        count = 0
        while current.next:
            count += 1
            current = current.next
        removal_target = count - n
        current = temp_head
        for _ in range(removal_target):
            current = current.next
        temp = current.next.next if current.next else None
        current.next = temp
        return temp_head.next
