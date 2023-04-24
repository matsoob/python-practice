
# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return True
        seen = set()
        # O(n) time complexity, O(n) space complexity
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
