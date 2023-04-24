import unittest
from solution import Solution

test_cases = [
    ("babad", "bab"),
    ("cAbbAd", "AbbA"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("", ""),
    ("ccc", "ccc"),
    ("aaaa", "aaaa")
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.longestPalindrome(input), output)

if __name__ == '__main__':
    unittest.main()
