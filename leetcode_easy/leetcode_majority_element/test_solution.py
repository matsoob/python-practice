import unittest
from solution import Solution

test_cases = [
    ([2,2,1,1,1,2,2], 2),
    ([3,2,3], 3),
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.majorityElement(input), output)

if __name__ == '__main__':
    unittest.main()
