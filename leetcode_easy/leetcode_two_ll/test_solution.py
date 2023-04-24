import unittest
from solution import Solution, ListNode


class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        a = ListNode(4)
        a.next = ListNode(1)
        b = ListNode(5)
        b.next = ListNode(6)
        b.next.next = ListNode(1)

        eight = ListNode(8)
        a.next.next = eight
        b.next.next.next = eight

        eight.next = ListNode(4)
        eight.next.next = ListNode(5)

        self.assertEqual(sol.getIntersectionNode(a, b), eight)

    def test_solution_no_intersection(self):
        sol = Solution()
        a = ListNode(4)
        a.next = ListNode(1)
        b = ListNode(5)
        b.next = ListNode(6)
        b.next.next = ListNode(1)
        self.assertEqual(sol.getIntersectionNode(a, b), None)

    def test_solution_space(self):
        sol = Solution()
        a = ListNode(4)
        a.next = ListNode(1)
        b = ListNode(5)
        b.next = ListNode(6)
        b.next.next = ListNode(1)

        eight = ListNode(8)
        a.next.next = eight
        b.next.next.next = eight

        eight.next = ListNode(4)
        eight.next.next = ListNode(5)

        self.assertEqual(sol.getIntersectionNodeSpaceEfficient(a, b), eight)

    def test_solution_no_intersection_space(self):
        sol = Solution()
        a = ListNode(4)
        a.next = ListNode(1)
        b = ListNode(5)
        b.next = ListNode(6)
        b.next.next = ListNode(1)
        self.assertEqual(sol.getIntersectionNodeSpaceEfficient(a, b), None)
    
if __name__ == '__main__':
    unittest.main()
