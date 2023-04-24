import unittest
from solution import Solution

test_cases = [
    ("A", 1),
    ("AB", 28),
    ("ZY", 701)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.titleToNumber(input), output)

if __name__ == '__main__':
    unittest.main()
