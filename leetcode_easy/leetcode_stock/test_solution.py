import unittest
from solution import Solution

test_cases = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.maxProfit(input), output)

if __name__ == '__main__':
    unittest.main()
