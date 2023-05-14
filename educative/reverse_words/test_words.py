import unittest
from words import reverse_words, reverse_words2

test_cases = [
    ("We love Python", "Python love We"),
    ("Hello     World", "World Hello")
]

class TestCase(unittest.TestCase):
    def test_solution(self):
        for input, output in test_cases:
            self.assertEqual(reverse_words(input), output)

    def test_solution_2(self):
        for input, output in test_cases:
            self.assertEqual(reverse_words2(input), output)

if __name__ == '__main__':
    unittest.main()
