import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 0 
        m = float("inf")
        r = max(piles)
       

        while l <= r:
            hr = 0 
            middle = (l+r)//2
            if middle == 0:
                break
            for p in piles:
                hr += math.ceil(p/middle)
    
            if hr > h:
                l = middle + 1
            else:
                m = min(m,middle)
                r = middle - 1
        if len(piles) == 1 and piles[0] == h and h == 1:
            return piles[0]
        return m

# time: O(nlogm); space: O(1) 