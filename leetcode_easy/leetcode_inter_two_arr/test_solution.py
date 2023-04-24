import unittest
from solution import Solution

test_cases = [
    (([1,2,2,1], [2,2]), [2,2]),
    (([4,9,5], [9,4,9,8,4]), [4,9])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.intersect(input[0], input[1]), output)

if __name__ == '__main__':
    unittest.main()
