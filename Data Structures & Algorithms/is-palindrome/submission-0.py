class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(char for char in s if char.isalnum())
        cleaned_string = cleaned_string.lower()
        n = len(cleaned_string)
        l, r = 0, n-1
        while (l <= r):
            if cleaned_string[l] != cleaned_string[r]:
                return False
            l += 1
            r -= 1
        return True