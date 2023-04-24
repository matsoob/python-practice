import unittest
from solution import Solution

test_cases = [
    (([1,2,3,4,5],[3,4,5,1,2]), 3),
    (([2,3,4],[3,4,3]), -1),
    (([0,0,0,1,2,0,5],[2,2,2,0,0,2,0]), 3),
    (([2],[2]), 0)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.canCompleteCircuit(input[0], input[1]), output)
    def test_solution_fast(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.canCompleteCircuitFaster(input[0], input[1]), output)

if __name__ == '__main__':
    unittest.main()
