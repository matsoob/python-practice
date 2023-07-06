# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import bisect

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_arr = []
        curr_sum = 0
        for num in nums:
            sum_arr.append(curr_sum)
            curr_sum += num
        all_sum = curr_sum
        if target > all_sum:
            return 0
        curr_min = len(nums)
        for i, num in enumerate(sum_arr):
            finding_over = num + target
            if all_sum < finding_over:
                break
            found_at = bisect.bisect_left(sum_arr, finding_over)
            curr_min = min(curr_min, found_at - i)
        return curr_min

