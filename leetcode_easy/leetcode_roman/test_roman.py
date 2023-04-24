import unittest

from roman import Solution

test_cases = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("CMXLIX", 949)
]

class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        for input, expectedResult in test_cases:
            self.assertEqual(solution.romanToInt(input), expectedResult)

if __name__ == "__main__":
    unittest.main()     