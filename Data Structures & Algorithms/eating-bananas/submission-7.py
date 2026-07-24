class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        limit = max(piles)
        rate = 1
        m = float("inf")
        

        while rate <= limit:
            middle = (rate + limit) // 2
            i = 0
            time = 0
            gathered = 0
            while i < len(piles):
                    time += math.ceil(piles[i] / middle)
                    gathered += piles[i]
                    i += 1
          
    
            if time > h:
                rate = middle + 1
            elif time <= h:
                m = min(m,middle)
                limit = middle - 1
        
        return m if m != float("inf") else 0
