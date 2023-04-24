import unittest
from solution import Solution

test_cases = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (8, 2),
    (9, 3),
    (15, 3),
    (59050, 243),
    (5559050, 2357),
    (2147483647, 46340)
]

class TestCase(unittest.TestCase):
    def test_square_root(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.mySqrt2(input), output)

if __name__ == '__main__':
    unittest.main()
