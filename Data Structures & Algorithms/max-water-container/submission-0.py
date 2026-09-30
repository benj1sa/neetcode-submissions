class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxwat = 0
        while l < r and l < len(heights) and r >= 0:
            wat = (r - l) * min(heights[r], heights[l])
            maxwat = max(maxwat, wat)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxwat