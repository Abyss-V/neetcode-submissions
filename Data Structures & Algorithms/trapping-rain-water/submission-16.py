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
                maxleft = max(maxleft,height[l])
            else:
                r -= 1
                if maxright - height[r] > 0:
                    res += maxright - height[r]
                maxright = max(maxright,height[r])

        return  res
    

#time: O(n); space: O(1)