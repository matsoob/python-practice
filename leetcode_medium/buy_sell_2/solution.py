# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0 
        profit = 0
        last_bought = 0
        pointer = 0
        while pointer < len(prices):
            if prices[last_bought] < prices[pointer]:
                profit += prices[pointer] - prices[last_bought]
                last_bought = pointer
            else:
                last_bought = pointer
            pointer += 1
        return profit