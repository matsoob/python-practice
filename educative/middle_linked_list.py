def get_middle_node(head):
    if not head:
        return None

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow