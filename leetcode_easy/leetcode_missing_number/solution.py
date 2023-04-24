# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O_n time complexity since we iterate thru nums once
        # constant space since we're keeping a couple of ints
        n = len(nums)
        expected_sum = (n + 1) * n / 2
        observed_sum = 0
        for i in nums:
            observed_sum += i
        return int(expected_sum - observed_sum)