import unittest
from solution import Solution

test_cases = [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
    ([3,5,4,8,0,0], 6),
    ([0,3,5,4,8,0,0], 9)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.maxProfit(input), output)

if __name__ == '__main__':
    unittest.main()
