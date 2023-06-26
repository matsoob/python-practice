# https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, curr_cite in enumerate(citations):
            if i + 1 > curr_cite:
                return i
        return i + 1
            
            
