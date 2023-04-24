import unittest

from number import solution_1, solution_2


test_cases = [
    (10, False),
    (-121, False),
    (121, True),
    (0, True),
    (1, True),
    (3333, True),
    (12121, True),
    (4555, False)
]

class Test(unittest.TestCase):
    def test_string_solution(self):
        for input, expectedResult in test_cases:
            self.assertEqual(solution_1(input), expectedResult)

    def test_string_solution(self):
        for input, expectedResult in test_cases:
            self.assertEqual(solution_2(input), expectedResult)

if __name__ == "__main__":
    unittest.main()     