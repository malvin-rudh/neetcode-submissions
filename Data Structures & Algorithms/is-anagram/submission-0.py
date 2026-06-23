class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Brute Force Approach:
            Use 2 for loops to keep on checking if the string s contains the letter 
            in sting t

            More efficient Approach:
            Use a hashmap and then use a for loop and go through the other one
        """
        
        if len(s) != len(t):
            return False
        
        n = len(s)
        s_hashmap = {}

        for i in range(n):
            s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1

        for i in range(n):
            if t[i] not in s_hashmap:
                return False
            s_hashmap[t[i]] -= 1
            if s_hashmap[t[i]] < 0:
                return False

        return True