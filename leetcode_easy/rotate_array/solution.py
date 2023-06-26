# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # constant space, O(n*k)
        for _ in range(k):
            temp = nums[-1]
            for i in range(len(nums)):
                nums[i], temp = temp, nums[i]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        temp = list()
        for i in range(len(nums)):
            new = (i + k) % len(nums)
            temp.append(nums[new])
            nums[new] = nums[i] if i < k else  temp[i-k]




