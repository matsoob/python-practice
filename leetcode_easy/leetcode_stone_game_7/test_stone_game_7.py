import unittest

from stone_game_7 import stoneGameVII

test_cases = [
    ([1,2], 2),
    ([5,3,1,4,2], 6),
    ([7,90,5,1,100,10,10,2], 122),
    ([2,3], 3),
    ([2,3,1], 2),
    ([792,195,697,271,743,51,836,322,135,550,399,182,988,25,395,254,480,931,513,772,798,102,110,915,794,330,597,220,789,462], 9066)
]

class TestGame(unittest.TestCase):

    def test_stoneGameVII(self):
        for input_arr, expected_output in test_cases:
            actual_output = stoneGameVII(input_arr)
            self.assertEqual(expected_output, actual_output)

    def test_empty(self):
        self.assertRaises(Exception,stoneGameVII, [])

    def test_one_stone(self):
        self.assertRaises(Exception,stoneGameVII, [1])


if __name__ == "__main__":
    unittest.main()     