import unittest

from pivot_index import Solution

test_cases = [
    ([5], 0),
    ([1,9,1], 1),
    ([], -1),
    ([1,2], -1),
]

class Test(unittest.TestCase):
    def test_string_solution(self):
        solution = Solution()
        for input, expectedResult in test_cases:
            self.assertEqual(solution.pivotIndex(input), expectedResult)

if __name__ == "__main__":
    unittest.main()     