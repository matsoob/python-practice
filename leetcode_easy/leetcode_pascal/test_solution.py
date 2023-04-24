import unittest
from solution import Solution

test_cases = [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (1, [[1]])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.generate(input), output)

if __name__ == '__main__':
    unittest.main()
