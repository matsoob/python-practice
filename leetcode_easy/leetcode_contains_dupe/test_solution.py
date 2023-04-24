import unittest
from solution import Solution

test_cases = [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.containsDuplicate(input), output)

if __name__ == '__main__':
    unittest.main()
