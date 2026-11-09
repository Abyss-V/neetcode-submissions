class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # A=l×w
        s = []
        m = 0

        for i,h in enumerate(heights):
            start = i
            while s and s[-1][0] > h:
                m = max(m,s[-1][0]*(i-s[-1][1]))
                start = s[-1][1]
                s.pop()
 
            s.append((h,start))
        for h,i in s:
            m = max(m,h*(len(heights)-i))
     
        return m
