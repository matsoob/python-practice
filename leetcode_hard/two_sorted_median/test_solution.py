import unittest
from solution import Solution

test_cases = [
    (([1,2], [3,4]), 2.5),
    (([1,3],[2]), 2)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.findMedianSortedArrays(input[0],input[1]), output)

if __name__ == '__main__':
    unittest.main()
