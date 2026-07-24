class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        mx = 0
        while i < j:
            diff = j - i
            mx = max(mx,min(heights[i] * diff, heights[j] * diff))
            if heights[i] * diff >= heights[j] * diff:
                j -= 1
            elif heights[i] * diff <= heights[j] * diff:
                i += 1
            
        return mx

