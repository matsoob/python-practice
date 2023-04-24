# https://leetcode.com/problems/power-of-three/
import math
import sys

class Solution:
    # Brute force
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1: 
            return True
        while n % 3 == 0:
            n /= 3
        return n == 1

    def isPowerOfThreeMath(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log(n) / math.log(3)
        return abs(round(x) - x) < 1e-10