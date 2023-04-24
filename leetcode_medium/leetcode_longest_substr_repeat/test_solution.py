import unittest
from solution import Solution

test_cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    (" ", 1),
    ("dvdf", 3)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.lengthOfLongestSubstring(input), output)

if __name__ == '__main__':
    unittest.main()
