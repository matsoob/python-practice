#https://leetcode.com/problems/find-pivot-index
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_of_all = sum(nums) # O_n
        running_left_total = 0
        last_index = len(nums) - 1
        curr_index = 0
        while curr_index <= last_index: # O_n
            curr_num = nums[curr_index]
            half = (sum_of_all - curr_num) / 2.0
            if half == running_left_total:
                return curr_index
            else:
                running_left_total += curr_num
                curr_index += 1
        return -1
