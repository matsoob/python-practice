import unittest
from solution import Solution

test_cases = [
    ([2,3,1,1,4], 2),
    ([2,3,0,1,4], 2),
    ([1], 0)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.jump(input), output)

if __name__ == '__main__':
    unittest.main()
