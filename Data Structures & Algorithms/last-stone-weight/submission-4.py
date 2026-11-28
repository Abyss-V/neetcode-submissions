class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = []
        for n in stones:
            heapq.heappush(s,n*-1)
        if len(stones) == 1:
            return stones[0]
        while 1 < len(s):
            n1 = -heapq.heappop(s)
            n2 = -heapq.heappop(s)

            if n1 > n2:
                heapq.heappush(s,(n1-n2)*-1)
            elif n2 > n1:
                heapq.heappush(s,(n2-n1)*-1)

        return -s[0] if len(s) else 0

#time:O(nlogn);space:O(n)