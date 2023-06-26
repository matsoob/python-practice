# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        last_checked = None
        to_fill = 0 
        for i in nums:
            if i != last_checked:
                nums[to_fill] = i
                to_fill += 1
            last_checked = i
        return to_fill

