import unittest
from solution import Solution

test_cases = [
    ([10,2], "210"),
    ([3,30,34,5,9], "9534330"),
    ([9,999,98], "999998")
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.largestNumber(input), output)

if __name__ == '__main__':
    unittest.main()
