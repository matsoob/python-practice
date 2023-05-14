import unittest
from solution import Solution

test_cases = [
    ("A man, a plan, a canal: Panama", True)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.func(input), output)

if __name__ == '__main__':
    unittest.main()
