class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""

        l, n = 0, len(s)
        t_map = {}
        window_map = {}

        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        res, res_len = [-1, -1], float("inf")
        matches, need = 0, len(t_map) 
        
        for r in range(len(s)):
            window_map[s[r]] = window_map.get(s[r], 0) + 1

            if s[r] in t_map and window_map[s[r]] == t_map[s[r]]:
                matches += 1
            
            while matches == need:
                if (r - l + 1) < res_len:
                    res[0], res[1] = l, r
                    res_len = r - l + 1

                window_map[s[l]] -= 1

                if s[l] in t_map and window_map[s[l]] < t_map[s[l]]:
                    matches -= 1
                    
                l += 1
            
        return s[res[0]:res[1]+1] if res_len != float("inf") else ""






