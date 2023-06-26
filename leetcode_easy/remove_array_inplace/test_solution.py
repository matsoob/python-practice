import unittest
from solution import Solution

test_cases = [
    (([1,2,3,2,5], 2), 3)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.removeElement(*input), output)

if __name__ == '__main__':
    unittest.main()
