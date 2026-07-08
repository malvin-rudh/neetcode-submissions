class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, n = 0, len(s)

        if n == 0:
            return 0

        window_hashmap = {}
        max_length = 0
        max_freq = 0

        # for r in range(n):
        #     window_hashmap[s[r]] = window_hashmap.get(s[r], 0) + 1
        #     most_freq_char = max(window_hashmap, key=window_hashmap.get)
        #     replacements = r - l + 1 - window_hashmap[most_freq_char]
        #     while ((replacements > k) and (l < r)):
        #         if s[l] != most_freq_char:
        #             replacements -= 1
        #         window_hashmap[s[l]] -= 1
        #         l += 1
        #     max_length = max(max_length, r - l + 1)
        # return max_length

        ## The problem: most frequent character is frozen across the whole while loop 

        for r in range(n):
            window_hashmap[s[r]] = window_hashmap.get(s[r], 0) + 1
            max_freq = max(max_freq, window_hashmap[s[r]])

            while ((r - l + 1) - max_freq) > k: ## this doesn't freeze the most_freq_char
                window_hashmap[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
