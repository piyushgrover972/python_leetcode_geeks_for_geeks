"""
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    Tags: Two Pointers; Easy;
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        sell = None
        buy = prices[0]

        i = 1
        while i < len(prices):

            # Buy if new day's price is lower than last buy day
            if prices[i] < buy:
                buy = prices[i]

            # If Price is greater than buy price, then there is possibility of selling
            elif prices[i] > buy:
                # Sell if this day gives better profit
                profit = max(profit, prices[i] - buy)

            i += 1

        return profit
