import unittest
from solution import Solution

test_cases = [
    ([3,0,1], 2),
    ([0,1], 2),
    ([9,6,4,2,3,5,7,0,1], 8)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.missingNumber(input), output)

if __name__ == '__main__':
    unittest.main()
