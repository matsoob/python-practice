import unittest
from solution import Solution

test_cases = [
    (("abc", "ahbgdc"), True),
    (("axc", "ahbgdc"), False)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.isSubsequence(*input), output)

if __name__ == '__main__':
    unittest.main()
