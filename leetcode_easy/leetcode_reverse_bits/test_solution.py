import unittest
from solution import Solution

test_cases = [
    (43261596, 964176192),
    (4294967293, 3221225471)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.reverseBits(input), output)

if __name__ == '__main__':
    unittest.main()
