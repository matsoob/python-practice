# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Note that you must do this in-place without making a copy of the array.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                swapped = False
                looking_at = i+1
                while not swapped and looking_at < len(nums):
                    if nums[looking_at] != 0:
                        temp = nums[i]
                        nums[i] = nums[looking_at]
                        nums[looking_at] = temp
                        swapped = True
                    else:
                        looking_at += 1
                if not swapped:
                    # Means we had a 0, went all the way to the end,
                    # didn't find another non-0 to swap with so we're done
                    break
    # Not great, worst case all the numbers are at the end


    def moveZeroes2(self, nums: List[int]) -> None:
        if not nums:
            return
        next_num = 0
        while nums[next_num] == 0 and next_num < len(nums):
            next_num += 1
            if next_num == len(nums):
                return
        for i in range(len(nums)):
            if next_num < i:
                next_num = i
                while nums[next_num] == 0 and next_num < len(nums):
                    next_num += 1
                    if next_num == len(nums):
                        return
            if nums[i] == 0:
                nums[i] = nums[next_num]
                nums[next_num] = 0
                while nums[next_num] == 0 and next_num < len(nums):
                    next_num += 1   
                    if next_num == len(nums):
                        return