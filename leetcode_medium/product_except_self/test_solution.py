import unittest
from solution import Solution

test_cases = [
    ([-1,1,0,-3,3], [0,0,9,0,0]),
    ([1,2,3,4], [24,12,8,6]),
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.productExceptSelf(input), output)

if __name__ == '__main__':
    unittest.main()
