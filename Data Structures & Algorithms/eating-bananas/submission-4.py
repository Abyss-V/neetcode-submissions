import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 0
        s = 0
        left = 0
        right = max(piles)
        m = float("inf")
        while left <= right:
            k = (left + right) // 2
            i = 0
            s = 0
            if k == 0:
                break
            while i < len(piles):
                s += math.ceil(piles[i]/k)
                i += 1

            if s > h:
                left = k + 1
            if s <= h:
                m = min(m,k)
                right = k  - 1
            
        return m

# solution with the help of video explanation and the complexity is:
# time: o(log(max(n)) * n)
# space: o(1)