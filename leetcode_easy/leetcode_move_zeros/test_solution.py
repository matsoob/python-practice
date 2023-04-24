import unittest
from solution import Solution

test_cases = [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
    ([], []),
    ([0,0,0,0,2],[2,0,0,0,0])

]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            sol.moveZeroes2(input)
            self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()
