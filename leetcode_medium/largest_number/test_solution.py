import unittest
from solution import Solution

test_cases = [
    ([10,2], "210"),
    ([3,30,34,5,9], "9534330"),
    ([9,999,98], "999998"),
    ([334, 324, 330, 33, 3], "334333330324"),
    ([0,0,0], "0"),
    ([1,1,1], "111"),
    ([432,43243], "43243432")
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.largestNumber2(input), output)

if __name__ == '__main__':
    unittest.main()
