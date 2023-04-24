import unittest
from solution import Solution

test_cases = [
    (27, True),
    (0, False),
    (243, True),
    (177146, False),
    (1594322, False)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.isPowerOfThreeMath(input), output)

if __name__ == '__main__':
    unittest.main()
