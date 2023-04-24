import unittest

from solution import Solution

test_cases = [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
    ([], ""),
    (["dodo","dog","dingbat"], "d"),
    (["catthew","catthew","catthew","catthew"], "catthew"),
    (["catthew"], "catthew"),
]

class Test(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        for input, expectedResult in test_cases:
            self.assertEqual(solution.longestCommonPrefix(input), expectedResult)
    def test_solution_2(self):
        solution = Solution()
        for input, expectedResult in test_cases:
            self.assertEqual(solution.longestCommonPrefixWithException(input), expectedResult)
    def test_solution_3(self):
        solution = Solution()
        for input, expectedResult in test_cases:
            self.assertEqual(solution.longestCommonPrefixNoException(input), expectedResult)

if __name__ == "__main__":
    unittest.main()     