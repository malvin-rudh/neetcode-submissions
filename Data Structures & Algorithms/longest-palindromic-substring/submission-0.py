class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            Notice that for each single letters, they are all palindrome
            For a particular palindrome, say:
                a_l , a_{l+1}, ... , a_{r-1}, a_{r}
            the string a_{l+1}, ... , a_{r-1} must also be a palindrome

            This looks like an interval DP problem, where the string at [l...r] depends on whether the string at [(l+1)...(r-1)] is a palindrome or not. 
            Definition: dp[l][r] = 1 if string at [l...r] is a palindrome, else 0
            Recursion:
                            1 if l == r
                dp[l][r] =  1 if dp[l+1][r-1] == 1 and s[l] == s[r]
                            0 otherwise
            Then, to check the longest palindromic substring, we can maintain a global max while calculating the dp array.
        """
        n = len(s)

        if n == 0:
            return ""

        dp = [[0] * n for _ in range(n)]
        max_len = 1
        start = 0

        ## Base case:
        for i in range(n):
            dp[i][i] = 1
            
        for length in range(2, n+1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                if length == 2:
                    if s[l] == s[r]:
                        dp[l][r] = 1
                else:
                    if s[l] == s[r] and dp[l+1][r-1] == 1:
                        dp[l][r] = 1

                if dp[l][r] == 1 and length > max_len:
                    max_len = length
                    start = l

        return s[start : start + max_len]