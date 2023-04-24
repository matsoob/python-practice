import unittest
from linked_list.linked_list import make_linkedlist, flatten_linkedlist
from solution import Solution, ListNode

test_cases = [
    ([1,2,3,4,5], [5,4,3,2,1]),
    ([1,2,3], [3,2,1]),
    ([],[]),
    ([4],[4])
]
    

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            result = sol.reverseList(make_linkedlist(input))
            result_list = flatten_linkedlist(result)
            self.assertEqual(result_list, output)

    def test_solution_2(self):
        sol = Solution()
        for input, output in test_cases:
            result = sol.reverseList2(make_linkedlist(input))
            result_list = flatten_linkedlist(result)
            self.assertEqual(result_list, output)

    def test_solution_3(self):
        sol = Solution()
        for input, output in test_cases:
            result = sol.reverseListRecursive(make_linkedlist(input))
            result_list = flatten_linkedlist(result)
            self.assertEqual(result_list, output)

if __name__ == '__main__':
    unittest.main()
