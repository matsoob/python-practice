import unittest
from solution import Solution

test_cases = [
    (3, ["1","2","Fizz"]),
    (5, ["1","2","Fizz","4","Buzz"]),
    (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        for input, output in test_cases:
            self.assertEqual(sol.fizzBuzz(input), output)

if __name__ == '__main__':
    unittest.main()
