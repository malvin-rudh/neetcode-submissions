class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        arr_s1 = [0] * 26
        arr_s2 = [0] * 26
        for s in s1:
            arr_s1[ord(s) - ord('a')] += 1
        
        for i in range(n1):
            arr_s2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(n1, n2):
            if arr_s1 == arr_s2:
                return True
            arr_s2[ord(s2[i - n1]) - ord('a')] -= 1
            arr_s2[ord(s2[i]) - ord('a')] += 1
        
        return arr_s1 == arr_s2

            