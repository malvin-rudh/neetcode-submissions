class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            Notice that since you cannot rob the 2 adjacent houses, then you can just see if it's more worth to rob the current house and the previous 2 houses or is it more worth to not rob
            the current house and instead rob the previous house.
            Definition: dp[i] represents the max amount of money to rob from house 0 to house i
            Recursion: dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        """

        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        dp = [0] * n
        
        ## Base Case:
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return max(dp)