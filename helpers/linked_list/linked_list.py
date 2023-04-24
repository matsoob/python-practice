
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_linkedlist(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for i in range(1, len(vals)):
        new_node = ListNode(vals[i])
        curr.next = new_node
        curr = new_node
    return head

def flatten_linkedlist(current: Optional[ListNode]) -> List[int]:
    if not current:
        return []
    vals = []
    while current:
        vals.append(current.val)
        current = current.next
    return vals
