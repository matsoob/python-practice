import unittest
from solution import Solution

test_cases = [
    (3, ["((()))","(()())","(())()","()(())","()()()"]),
    (1, ["()"])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(set(sol.generateParenthesis(input)), set(output))

if __name__ == '__main__':
    unittest.main()
