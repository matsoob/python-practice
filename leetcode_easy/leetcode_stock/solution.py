# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        observed_max = 0
        min_price_thus_far = prices[0]
        for price in prices:
            if price < min_price_thus_far:
                min_price_thus_far = price
            if price - min_price_thus_far > observed_max:
                observed_max = price - min_price_thus_far
            
        return observed_max