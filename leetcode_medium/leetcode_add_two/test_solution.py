import unittest
from solution import Solution
from linked_list.linked_list import make_linkedlist, flatten_linkedlist

test_cases = [
    (([2,4,3], [5,6,4]), [7,0,8]),
    (([0], [0]), [0]),
    (([9,9,9,9,9,9,9], [9,9,9,9]), [8,9,9,9,0,0,0,1])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            l1 = make_linkedlist(input[0])
            l2 = make_linkedlist(input[1])
            result = sol.addTwoNumbers2(l1, l2)
            self.assertEqual(flatten_linkedlist(result), output)

if __name__ == '__main__':
    unittest.main()
