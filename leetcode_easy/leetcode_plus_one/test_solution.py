import unittest
from solution import Solution

test_cases = [
    ([1,2,3], [1,2,4]),
    ([4,3,2,2], [4,3,2,3]),
    ([4,3,9,9], [4,4,0,0]),
    ([9], [1,0])
]

class TestCase(unittest.TestCase):
    # def test_solution(self):
    #     solution = Solution()
    #     for input, output in test_cases:
    #         self.assertEqual(solution.plusOne(input),output)

    def test_solution2(self):
        solution = Solution()
        for input, output in test_cases:
            self.assertEqual(solution.plusOne2(input), output)

if __name__ == '__main__':
    unittest.main()