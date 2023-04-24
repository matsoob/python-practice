import unittest
from solution import Solution

test_cases = [
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("", []),
    ("2", ["a","b","c"])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(set(sol.letterCombinations(input)), set(output))

if __name__ == '__main__':
    unittest.main()
