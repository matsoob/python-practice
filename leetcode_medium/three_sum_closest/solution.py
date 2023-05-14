# https://leetcode.com/problems/3sum-closest/
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-2):
            num = sorted_nums[i]
            left = i + 1
            right = len(sorted_nums) - 1
            while left != right:
                current = num + sorted_nums[left] + sorted_nums[right]
                if current == target:
                    return target
                if closest is None or abs(current - target) < abs(closest - target):
                    closest = current
                if current < target:
                    left += 1
                if current > target:
                    right -= 1
        return closest