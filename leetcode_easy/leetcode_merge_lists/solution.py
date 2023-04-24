# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        base_list, other_list = (list1, list2) if list1.val <= list2.val else (list2, list1)
        head = base_list
        while other_list is not None:
            while base_list.next is not None and base_list.next.val <= other_list.val:
                base_list = base_list.next
            temp = base_list.next
            base_list.next = other_list
            other_list = other_list.next
            base_list.next.next = temp

        return head


    def mergeTwoListsNewList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        
        curr.next = list1 if list1 else list2

        return dummy.next


        
