# https://leetcode.com/problems/random-pick-with-weight/
from bisect import bisect_right
import math
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.weighted_intervals = []
        running_sum = 0
        for x in w:
            running_sum += x
            self.weighted_intervals.append(running_sum)
        self.total = sum(w)
        # [0, 2, 8, 0, 4] -> [0, 2, 10, 10, 14] # finding first one larger than me

    def pickIndex(self) -> int:
        ran = random.random() * self.total # 0<x<=1 so 0<ran<=self.weight
        first_greater_than_index = bisect_right(self.weighted_intervals, ran)
        return first_greater_than_index
        

        
if __name__ == '__main__':
    sol = Solution([0, 2, 8, 0, 4])
    sol.pickIndex()