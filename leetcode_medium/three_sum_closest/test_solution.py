import unittest
from solution import Solution

test_cases = [
    (([-1,2,1,-4], 1), 2),
    (([0,0,0], 1), 0)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.threeSumClosest(input[0], input[1]), output)

if __name__ == '__main__':
    unittest.main()
