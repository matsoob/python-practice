# https://leetcode.com/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unclaimed = set()
        for num in nums:
            if num in unclaimed:
                unclaimed.remove(num)
            else:
                unclaimed.add(num)
        return unclaimed.pop()