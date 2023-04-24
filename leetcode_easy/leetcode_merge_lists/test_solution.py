from typing import List, Optional
import unittest
from solution import Solution, ListNode

test_cases = [
    (([1,2], [3]), [1,2,3]),
    (([1,2,4], [1,3,4]), [1,1,2,3,4,4]),
    (([],[]), []),
    (([], [0]), [0]),
    (([2,3,4,4,5,77,88, 103], [0, 100, 101, 102]), [0, 2, 3, 4, 4, 5, 77, 88, 100, 101, 102, 103])
]

def hydrate(arr: List[int]) -> Optional[ListNode]:
    if len(arr) == 0:
        return
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])
        curr.next = new_node
        curr = new_node
    return head

class Test(unittest.TestCase):
    def test_solution(self):
        soluton = Solution()
        for input, expectedResult in test_cases:
            result_head = soluton.mergeTwoLists(hydrate(input[0]), hydrate(input[1]))
            result = []
            while result_head is not None:
                result.append(result_head.val)
                result_head = result_head.next
            self.assertEqual(result, expectedResult)

    def test_solution_2(self):
        soluton = Solution()
        for input, expectedResult in test_cases:
            result_head = soluton.mergeTwoListsNewList(hydrate(input[0]), hydrate(input[1]))
            result = []
            while result_head is not None:
                result.append(result_head.val)
                result_head = result_head.next
            self.assertEqual(result, expectedResult)

if __name__ == "__main__":
    unittest.main()

