# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        current_steps = 0
        head_new_range = 0
        tail_new_reachable = 0
        while tail_new_reachable < len(nums) - 1:
            current_steps += 1
            next_farthest = tail_new_reachable
            for i in range(head_new_range, tail_new_reachable + 1):
                next_farthest = max(nums[i] + i, next_farthest)
            if next_farthest >= len(nums) - 1:
                return current_steps
            head_new_range, tail_new_reachable = tail_new_reachable + 1, next_farthest
        return current_steps
        




