# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = list()
        for _ in range(32):
            bits.append(n % 2)
            n = n // 2
        reversed = 0 
        for i in range(32):
            reversed = bits[i] + reversed*2
        return reversed
    
    def reverseBitsBinary(self, n: int) -> int:
        # TODO: review this
        output=0
        for i in range(32):
            bits = n & 1
            output = output | bits << (31-i)
            n = n >> 1
        return output