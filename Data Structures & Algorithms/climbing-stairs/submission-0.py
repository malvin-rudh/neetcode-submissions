class Solution:
    def climbStairs(self, n: int) -> int:
        """
            Notice that in order to reach staircase i, it would either be from 2 steps back or 1 step back
            dp[i-1] would mean the number of ways to climb staircase i
            dp[i] = dp[i-1] + dp[i-2]
            Base Case: dp[0] = 1, dp[1] = 1
        """
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

