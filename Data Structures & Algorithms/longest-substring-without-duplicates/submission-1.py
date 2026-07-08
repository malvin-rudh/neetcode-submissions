class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        l = 0
        window_set = set([s[0]])
        max_length = 1

        for r in range(1, n):
            while (s[r] in window_set) and (l <= r):
                window_set.remove(s[l])
                l += 1
            window_set.add(s[r])
            curr_length = r - l + 1
            max_length = max(max_length, curr_length)
        
        return max_length
