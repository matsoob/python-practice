import unittest
from three import find_sum_of_three

test_cases = [
    (([1,-1,0], -1), False),
    (([3,7,1,2,8,4,5], 10), True),
    (([3,7,1,2,8,4,5], 21), False),
    (([-1,2,1,-4,5,-3], -8), True)
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        for input, output in test_cases:
            self.assertEqual(find_sum_of_three(input[0], input[1]), output)

if __name__ == '__main__':
    unittest.main()
