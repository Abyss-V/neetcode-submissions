class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        mx = 0
        while i < j:
            mx = max(mx,min(heights[i] * len(heights[i:j]), heights[j] * len(heights[i:j])))
            if heights[i] * len(heights[i:j]) >= heights[j] * len(heights[i:j]):
                j -= 1
            elif heights[i] * len(heights[i:j]) <= heights[j] * len(heights[i:j]):
                i += 1
            
        return mx