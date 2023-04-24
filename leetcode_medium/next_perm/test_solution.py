import unittest
from solution import Solution

test_cases = [
    ([1,2,3], [1,3,2]),
    ([1,2,3], [1,3,2]),
    ([3,2,1], [1,2,3]),
    ([1,3,2], [2,1,3]),
    ([1,1,5], [1,5,1]),
    ([1,3,2,0], [2,0,1,3]),
    ([2,3,2,0], [3,0,2,2]),
    ([1,1],[1,1])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            sol.nextPermutation(input)
            self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()
