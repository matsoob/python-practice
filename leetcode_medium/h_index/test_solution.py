import unittest
from solution import Solution

test_cases = [
    ([3,0,6,1,5], 3),
    ([1,3,1], 1),
    ([1], 1),
    ([10, 9, 8, 7], 4)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.hIndex(input), output)

if __name__ == '__main__':
    unittest.main()
