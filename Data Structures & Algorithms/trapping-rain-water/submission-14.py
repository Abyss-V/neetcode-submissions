class Solution:

    def trap(self, height: List[int]) -> int:
        

        l = 0
        r = len(height) - 1
        maxleft = height[l]
        maxright = height[r]
        res = 0
 
        while l < r:
            if maxleft <= maxright:
                l += 1
                
                if maxleft - height[l] > 0:
                    res += maxleft - height[l]
                maxleft = max(height[l],maxleft)
                
            else:
                r -= 1
                maxright = max(height[r],maxright)
                if maxright - height[r] > 0:
                    res += maxright - height[r]
                
        return res