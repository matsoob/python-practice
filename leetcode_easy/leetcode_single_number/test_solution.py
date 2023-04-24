import unittest
from solution import Solution

test_cases = [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.singleNumber(input), output)

if __name__ == '__main__':
    unittest.main()
