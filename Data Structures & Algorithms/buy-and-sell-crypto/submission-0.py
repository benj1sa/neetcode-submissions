class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = [0] * len(prices)
        min_price = float('inf')
        for i, p in enumerate(prices):
            min_price = min(min_price, p)
            low[i] = min_price
        max_profit = 0
        for i, n in enumerate(prices):
            profit = n - low[i]
            max_profit = max(max_profit, profit)
        return max_profit