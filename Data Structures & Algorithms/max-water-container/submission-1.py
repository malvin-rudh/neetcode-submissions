class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float("-inf")
        l, r = 0, len(heights)-1
        while (l < r):
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)
            if heights[l] >= heights[r]:
                r-= 1
            elif heights[l] < heights[r]:
                l += 1
        return max_area
