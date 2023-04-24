import unittest
from solution import Solution

test_cases = [
    ("()", True),
    ("()[]\{\}", True),
    ("(]", False),
    ("(((((()))))", False),
    ("(((((())))))", True),
    ("((((((", False),
    (")", False)
]

class TestCases(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        for input, expectedResult in test_cases:
            self.assertEqual(solution.isValid_list(input), expectedResult)

    def test_solution_2(self):
        solution = Solution()
        for input, expectedResult in test_cases:
            self.assertEqual(solution.isValid_deque(input), expectedResult)

if __name__ == "__main__":
    unittest.main()     