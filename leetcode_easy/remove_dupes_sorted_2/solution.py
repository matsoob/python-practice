# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        last = None
        last_last = None
        to_fill = 0
        for i in nums:
            if last != last_last or last != i:
                nums[to_fill] = i
                to_fill += 1
            last_last, last = last, i
        return to_fill
