class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq.heapify_max(stones)
            maxi = heapq.nlargest(2, stones)
            if maxi[0] == maxi[1]:
                heapq.heappop_max(stones)
                heapq.heappop_max(stones)
            else:
                heapq.heappop_max(stones)
                heapq.heappop_max(stones)
                heapq.heappush(stones,maxi[0] - maxi[1])
        if stones == []:
            return 0
        return max(stones)
        
         