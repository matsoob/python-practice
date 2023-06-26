import unittest
from solution import Solution

test_cases = [
    (([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4]),
    (([-1,-100,3,99], 2), [3,99,-1,-100])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            sol.rotate2(*input)
            self.assertEqual(input[0], output)

if __name__ == '__main__':
    unittest.main()
