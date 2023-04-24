# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Start with naive impl
        # this is n^2 time complexity, constant space complexity
        max_area = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(area, max_area)
        return max_area
    
    def maxAreaEfficient(self, height: List[int]) -> int:
        max_area = 0
        start_pointer = 0
        end_pointer = len(height) - 1
        while start_pointer != end_pointer:
            current_area = (end_pointer - start_pointer) * min(height[end_pointer], height[start_pointer])
            max_area = max(current_area, max_area)
            if height[end_pointer] > height[start_pointer]:
                start_pointer += 1
            else:
                end_pointer -= 1
        return max_area
