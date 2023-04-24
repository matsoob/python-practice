import unittest
from solution import Solution

test_cases = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.firstUniqChar(input), output)

if __name__ == '__main__':
    unittest.main()
