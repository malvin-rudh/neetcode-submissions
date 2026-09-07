class Solution:
    def numDecodings(self, s: str) -> int:
        """
            Notice that we can solve this subproblem by subproblem, i.e. little by little.
            The idea is that at any number, we try to look back the previous number, if it's a 1 then, we know that there
            are 2 ways to decode this 2 current numbers. And, what we can do is just add +1 to the number of ways to decode
            the previous number. The reason is simple because let's say that the number of ways to decode the previous number
            is 3, then because this previous number is 1 and the next number is say x, it adds another combination as if we 
            combine 1x. If it's a 0, then we should -1, because the previous number and 0 cannot be combined together. Else, if it's a 2 for the previous number, similarly we do +1 if the current number is <= 6, else we don't add it. If the 
            previous number is > 2, then we just skip it and go to the next. By skipping I mean just put the same number as the
            previous.

            Definition:
            dp[i] represents the no. of ways to decode the first i characters
        """

        n = len(s)

        if n == 0:
            return 0

        if s[0] == '0':
            return 0

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            two_digits = int(s[i-2:i])    
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[n]