import unittest
from solution import Solution
from linked_list.linked_list import make_linkedlist, flatten_linkedlist
test_cases = [
    (([1,2,3,4,5], 2), [1,2,3,5]),
    (([1], 1), []),
    (([1,2],1), [1]),
     (([],1), [])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            input_list = make_linkedlist(input[0])
            res = sol.removeNthFromEnd(input_list, input[1])
            res_flat = flatten_linkedlist(res)
            self.assertEqual(res_flat, output)

if __name__ == '__main__':
    unittest.main()
