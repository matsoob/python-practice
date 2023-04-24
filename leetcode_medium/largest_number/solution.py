# https://leetcode.com/problems/largest-number/
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        leading_dig_map = dict()
        for i in nums:
            i_str = str(i)
            leading_digit = i_str[0]
            if leading_digit in leading_dig_map:
                leading_dig_map[leading_digit].add(i_str)
            else:
                leading_dig_map[leading_digit] = set([i_str])
        keys = list(leading_dig_map.keys())
        keys.sort(reverse=True)
        
        result = ''
        for key in keys:
            figs = leading_dig_map.get(key)
            # TODO：
            

