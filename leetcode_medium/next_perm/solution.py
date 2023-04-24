# https://leetcode.com/problems/next-permutation/
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        swapped = False
        n = len(nums)
        pointer = n-2
        while pointer >= 0:
            if nums[pointer] >= nums[pointer+1]:
                pointer -= 1
            else:
                # do_swap
                swap_pointer = n - 1
                # found next largest element in what we've iterated over already
                while nums[swap_pointer] <= nums[pointer]:
                    swap_pointer -= 1
                nums[swap_pointer], nums[pointer] = nums[pointer], nums[swap_pointer]
                left_pointer = pointer + 1
                right_pointer = n - 1
                while left_pointer <= right_pointer:
                    nums[right_pointer], nums[left_pointer] = nums[left_pointer], nums[right_pointer]
                    left_pointer += 1
                    right_pointer -= 1
                swapped = True
                break
        if not swapped:
            nums.sort()

                


            
        
        
