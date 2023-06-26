import unittest
from solution import Solution

test_cases = [
    ('abbaca', 'ca'),
    ('abba', ''),
    ('annccad', 'd'),
    ('azxxzy', 'ay')
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.removeDuplicates(input), output)

if __name__ == '__main__':
    unittest.main()
