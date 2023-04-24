import unittest
from solution import Solution


test_cases = [
    (("sadbutsad", "sad"), 0),
    (("catthew", "cat"), 0),
    (("catthew", "sad"), -1),
    (("catsad", "sad"), 3),
]

class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        for inputs, expected_result in test_cases:
            self.assertEqual(expected_result, solution.strStr(inputs[0], inputs[1]))

if __name__ == '__main__':
    unittest.main()