import unittest
from solution import Solution

test_cases = [
    (["h","e","l","l","o"], ["o","l","l","e","h"]),
    (["H","a","n","n","a","h"], ["h","a","n","n","a","H"])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            sol.reverseString(input)
            self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()
