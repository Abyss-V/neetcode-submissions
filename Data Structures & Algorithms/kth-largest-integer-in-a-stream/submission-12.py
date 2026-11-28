class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        heapq.heapify(self.minheap)
        for n in nums:
            heapq.heappush(self.minheap,n)
            if len(self.minheap) > k:
                heapq.heappop(self.minheap)
        self.k=k

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minheap,val)
        print(self.minheap)
        if len(self.minheap) > self.k:
            print("m",self.minheap)
            heapq.heappop(self.minheap)
        return self.minheap[0]
