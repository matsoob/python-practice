import unittest
from solution import Solution

test_cases = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.isAnagram(input[0], input[1]), output)

if __name__ == '__main__':
    unittest.main()
