import unittest
from solution import Solution

test_cases = [
    ("{a,b}c{d,e}f", ["acdf","acef","bcdf","bcef"])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.expand(input), output)

if __name__ == '__main__':
    unittest.main()
