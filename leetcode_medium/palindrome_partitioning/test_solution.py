import unittest
from solution import Solution

test_cases = [
    ("aabba", [["a","a","b", "b", "a"],
               ["aa","b", "b", "a"], 
               ["a", "a", "bb", "a"], 
               ["aa", "bb", "a"],
               ["a", "abba"]]),
    ("a",  [["a"]])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.partition(input), output)

if __name__ == '__main__':
    unittest.main()
