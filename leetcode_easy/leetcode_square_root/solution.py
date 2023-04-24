import math
# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt_forbidden(self, x: int) -> int:
        # You must not use any built-in exponent function or operator.
        return int(math.sqrt(x))
    
    def mySqrt(self, x: int) -> int:
        curr = 0
        # For  0 <= x <= 2^31 - 1, the max this linear search could run for is 2^15 (50k ish)
        # Generally it will be O_sqrt(x) which isn't terrible...
        while True:
            # avoid overflow
            if (curr + 1) > x / (curr + 1):
                return curr
            else:
                curr += 1

    def mySqrt2(self, x: int) -> int:
        if x <= 1:
            return x
        low = 0
        higher_bound = x 
        while low < higher_bound - 1:
            mid = int((low + higher_bound) / 2)
            if mid > x/mid:
                higher_bound = mid
            elif mid < x/mid:
                low = mid
            else:
                return mid
        return low