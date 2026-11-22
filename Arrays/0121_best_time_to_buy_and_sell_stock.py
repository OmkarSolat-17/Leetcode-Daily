# Problem: 121. Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Pattern: Greedy / One Pass
# Time: O(n)
# Space: O(1)
# Runtime: 33ms (Beats 86.31%) | Memory: 18.96MB (Beats 79.57%)


class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit