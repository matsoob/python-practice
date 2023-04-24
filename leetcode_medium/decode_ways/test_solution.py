import unittest
from solution import Solution

test_cases = [
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("11106", 2),
    ("1110600", 0),
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.numDecodings(input), output)

if __name__ == '__main__':
    unittest.main()
