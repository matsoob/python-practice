import unittest
from solution import Solution

test_cases = [
    ("52233", 4),
    ("5494", 4),
    ("1111111", 2),
    ("0001", 3),
    ("0010", 4)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.longestSemiRepetitiveSubstring(input), output)

if __name__ == '__main__':
    unittest.main()
