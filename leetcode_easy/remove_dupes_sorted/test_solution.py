import unittest
from solution import Solution

test_cases = [
    ([1,1,2], 2),
    ([0,0,1,1,1,2,2,3,3,4], 5)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.removeDuplicates(input), output)

if __name__ == '__main__':
    unittest.main()
