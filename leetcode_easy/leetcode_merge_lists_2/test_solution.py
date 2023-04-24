import unittest
from solution import Solution
test_cases = [
    (([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6]),
    (([1], 1, [], 0), [1]),
    (([1, 0, 0, 0, 0, 0, 0], 1, [0,1,1,3,5,7], 6), [0,1,1,1,3,5,7])
]

class TestCase(unittest.TestCase):
    # def test_solution(self):
    #     sol = Solution()
    #     for input, output in test_cases:
    #         copy_of_array = input[0].copy()
    #         sol.merge(copy_of_array, input[1], input[2], input[3])
    #         self.assertEqual(
    #             copy_of_array,
    #             output
    #         )

    def test_solution2(self):
        sol = Solution()
        for input, output in test_cases:
            copy_of_array = input[0].copy()
            sol.merge3(copy_of_array, input[1], input[2], input[3])
            self.assertEqual(
                copy_of_array,
                output
            )
if __name__ == '__main__':
    unittest.main()