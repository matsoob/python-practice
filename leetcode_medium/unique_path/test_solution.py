import unittest
from solution import Solution

test_cases = [
    ((3,7), 28),
    ((3,2), 3)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.uniquePaths(input[0], input[1]), output)

if __name__ == '__main__':
    unittest.main()
