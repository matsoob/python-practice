import unittest
from solution import Solution

test_cases = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.maxArea(input), output)

    def test_solution2(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.maxAreaEfficient(input), output)

if __name__ == '__main__':
    unittest.main()
