class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # l, r = 0, n-1
        # while (height[l] == 0):
        #     l += 1
        # while (height[r] == 0):
        #     r -= 1

        # max_left = height[l]
        # max_right = height[r]
        
        max_left = [0] * n
        max_right = [0] * n

        curr_max_left = 0
        curr_max_right = 0
        
        for l in range(n):
            if height[l] > curr_max_left:
                curr_max_left = height[l]
            max_left[l] = curr_max_left
        for r in range(n-1, -1, -1):
            if height[r] > curr_max_right:
                curr_max_right = height[r]
            max_right[r] = curr_max_right

        total_sum = 0
        for i in range(n):
            total_sum += max(min(max_left[i], max_right[i]) - height[i], 0)
        
        return total_sum


