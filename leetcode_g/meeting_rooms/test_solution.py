import unittest
from solution import Solution

test_cases = [
    ([[0,30],[5,10],[15,20]], 2),
    ([[7,10],[2,4]], 1)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.minMeetingRooms(input), output)

if __name__ == '__main__':
    unittest.main()
