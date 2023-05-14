# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        one_pointer = 0
        two_pointer = 0
        median_pos = total_len // 2
        is_odd = total_len % 2 == 1
        for i in range(median_pos):
            if one_pointer >= len(nums1):
                two_pointer += 1
            elif two_pointer >= len(nums2):
                one_pointer += 1
            elif nums1[one_pointer] < nums2[two_pointer]:
                one_pointer += 1
            else:
                two_pointer += 1
        
        if one_pointer < len(nums1) and two_pointer < len(nums2):
            