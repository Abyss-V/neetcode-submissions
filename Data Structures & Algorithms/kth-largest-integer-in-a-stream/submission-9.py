class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = nums
        heapq.heapify(self.l)
        print(self.l)
        self.k=k

    def add(self, val: int) -> int:
        heapq.heappush(self.l,val)
        n = []
        while len(self.l) > self.k:
            p = heapq.heappop(self.l)
            n.append(p)
        print(self.l)
        r = self.l[-self.k]
        for p in n:
            heapq.heappush(self.l,p)
        return r
