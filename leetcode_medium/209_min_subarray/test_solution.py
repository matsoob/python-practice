import unittest
from solution import Solution

test_cases = [
    ((7, [2,3,1,2,4,3]), 2),
    ((4, [1,4,4]), 1),
    ((11, [1,1,1,1,1,1,1,1]), 0)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.minSubArrayLen(*input), output)

if __name__ == '__main__':
    unittest.main()
