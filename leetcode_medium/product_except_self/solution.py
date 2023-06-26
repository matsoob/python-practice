# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()
        current = 1
        for num in nums:
            result.append(current)
            current *= num
        current = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * current
            current *= nums[i]
        return result