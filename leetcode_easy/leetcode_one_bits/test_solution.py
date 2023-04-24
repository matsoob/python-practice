import unittest
from solution import Solution

test_cases = [
    (0b00000000000000000000000000001011, 3),
    (0b00000000000000000000000010000000, 1),
    (0b11111111111111111111111111111101, 31),
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.hammingWeight(input), output)

if __name__ == '__main__':
    unittest.main()
