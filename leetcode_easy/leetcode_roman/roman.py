# https://leetcode.com/problems/roman-to-integer/


LOOKUP = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
class Solution:

    def romanToInt(self, s: str) -> int:
        curr_sum = 0
        last_int = None
        for char in s:
            looked_up_int = LOOKUP[char]
            curr_sum += looked_up_int
            if last_int is not None and last_int < looked_up_int:
                curr_sum -= (last_int*2)
            last_int = looked_up_int
        return curr_sum