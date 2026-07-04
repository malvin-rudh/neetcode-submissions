class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        max_profit = 0

        for r in range(n):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
        return max_profit
        