import unittest
from solution import Solution, ListNode

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
       
        three = ListNode(3)
        two = ListNode(2)
        three.next = two
        two.next = ListNode(0)
        two.next.next = ListNode(-4)
        two.next.next.next = two

        self.assertEqual(sol.hasCycle(three), True)

if __name__ == '__main__':
    unittest.main()
