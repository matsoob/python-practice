# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        pointer = 0
        reachable = [False] * len(nums)
        reachable[0] = True
        while pointer < len(nums):
            if reachable[pointer] and nums[pointer] > 0:
                for i in range(1, nums[pointer]+1):
                    if pointer + i < len(nums):
                        reachable[pointer + i] = True
            pointer += 1
        return reachable[-1]

    def canJump2(self, nums: List[int]) -> bool:
        if not nums:
            return True
        pointer = 0
        max_reachable = 0
        while pointer < len(nums):
            if max_reachable >= pointer:
                max_reachable = max(max_reachable, pointer + nums[pointer])
            else:
                return max_reachable >= len(nums) - 1
            pointer += 1
        return max_reachable >= len(nums) - 1