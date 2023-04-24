# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        current = n
        def step(m: int) -> int:
            sum = 0
            while m:
                sum += (m % 10) ** 2
                m = m // 10
            return sum
        while current not in seen:
            seen.add(current)
            current = step(current)
            if current == 1:
                return True
        return False
        
    