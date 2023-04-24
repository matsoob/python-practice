import unittest
from solution import Solution
from linked_list.linked_list import make_linkedlist

test_cases = [
    ([1,2,2,1], True),
    ([1,2], False),
    ([1], True),
    ([], True),
    ([1,2,3,4,4,5,6,5,4,4,3,2,1], True)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            input_ll = make_linkedlist(input)
            self.assertEqual(sol.isPalindromeSimple(input_ll), output)

if __name__ == '__main__':
    unittest.main()
