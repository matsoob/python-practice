# https://leetcode.com/problems/plus-one/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # We're manipulating the input array here
        # For python it will pass a List[int] by reference so it will modify the object (visible to caller)
        # which probably isn't desired here
        if not digits:
            return [1]
        carrying = True
        curr_index = len(digits) - 1
        while carrying:
            if curr_index < 0:
                digits.insert(0, 1)
                carrying = False
            elif digits[curr_index] < 9:
                digits[curr_index] += 1
                carrying = False
            else:
                digits[curr_index] = 0
                curr_index -= 1
        return digits
    
    def plusOne2(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        incremented_digits = digits.copy()
        carrying = True
        curr_index = len(incremented_digits) - 1
        while carrying:
            if curr_index < 0:
                incremented_digits.insert(0, 1)
                carrying = False
            elif incremented_digits[curr_index] < 9:
                incremented_digits[curr_index] += 1
                carrying = False
            else:
                incremented_digits[curr_index] = 0
                curr_index -= 1
        return incremented_digits