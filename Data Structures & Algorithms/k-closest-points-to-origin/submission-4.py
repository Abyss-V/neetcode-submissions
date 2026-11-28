import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        heapq.heapify(minheap)
        f = {}
        for p in points:
            heapq.heappush(minheap,(math.sqrt((0-p[0])**2+(0-p[1])**2)*-1,p))
        print(minheap)
        while len(minheap) > k:
            p = heapq.heappop(minheap)
        print(minheap)
        return [m[1] for m in minheap]
    
# time:O(n log k+1) its equivalent to O(n logk); space:O(k)