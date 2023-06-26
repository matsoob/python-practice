
# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        to_fill = 0
        to_check = 0
        while to_check < len(nums):
            if nums[to_check] != val:
                nums[to_fill] = nums[to_check]
                to_fill += 1
            to_check += 1
        return to_fill
            
