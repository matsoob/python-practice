import unittest
from solution import Solution

test_cases = [
    (19, True),
    (2, False),
    (1, True),
    (0, False),
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.isHappy(input), output)

if __name__ == '__main__':
    unittest.main()
