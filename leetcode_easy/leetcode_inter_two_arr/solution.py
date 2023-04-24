# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        count_1 = dict()
        count_2 = dict()
        # Goes through nums1 once, O_n
        for i in nums1:
            if i in count_1:
                count_1[i] += 1
            else:
                count_1[i] = 1
        # Goes through nums2 once, O_n
        for i in nums2:
            if i in count_2:
                count_2[i] += 1
            else:
                count_2[i] = 1
        
        # Goes through keys of dict, O_n
        for key, _ in count_1.items():
            if key in count_2:
                occurance = min(count_1[key], count_2[key])
                result.extend(key for _ in range(occurance))
        # O_n space complexity, O_n time complexity
        return result
    

# What if the given array is already sorted? 
# How would you optimize your algorithm?
# If both were sorted, you'd still need to iterate through at least one
# (potential to use binary search on other if size difference is large)
# but wouldn't need to store state (just append results as you go) 
# So could save on space complexity.
# What if nums1's size is small compared to nums2's size? 
# Which algorithm is better?
# What if elements of nums2 are stored on disk, 
# and the memory is limited such that you cannot load all elements into the memory at once?