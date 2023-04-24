# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # assuming it always exists
        counts = dict()
        # O_n to iterate over all numbers
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        max_key = None
        max_occurance = 0
        # O_n to iterate over key/value pairs
        for key, value in counts.items():
            if value > max_occurance:
                max_key = key
                max_occurance = value
        # O_n space, O_n time
        return max_key

