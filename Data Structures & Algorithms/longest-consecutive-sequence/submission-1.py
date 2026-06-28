class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        max_len = float("-inf")
        for num in nums:
            if (num - 1) in nums:
                continue
            temp = num + 1
            curr_len = 1
            while (temp in nums):
                curr_len += 1
                temp += 1
            max_len = max(max_len, curr_len)
        
        return max_len
