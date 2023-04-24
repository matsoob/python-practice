import unittest

from game import game_recursion


test_cases = [
    ([5,3,4,5], True),
    ([3,7,2,3], True),
    ([1,2,3,4,4,5,65,6,6,7,7,8,8,9,5,4,3,4,5,6,67,7,8,4,2,2,6,4,5,45,3,4,5,6,6,7,7,7,34,3], True)
]

class Test(unittest.TestCase):
    def test(self):
        for input_arr, expectedResult in test_cases:
            self.assertEqual(game_recursion(input_arr), expectedResult)

if __name__ == "__main__":
    unittest.main()     