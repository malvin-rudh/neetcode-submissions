class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            To reach step[i], it's only either from 1 step back or 2 steps back
            dp[i] represents the cost to reach step i
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            Base Case is dp[0], dp[1] = 0, 0
        """
        n = len(cost)
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 0

        for i in range(2, n+1):
            # if i == 2:
            #     dp[i] = 0
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]
        