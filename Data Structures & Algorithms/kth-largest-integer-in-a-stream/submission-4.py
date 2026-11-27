class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = nums
        heapq.heapify(self.l)
        self.k=k

    def add(self, val: int) -> int:
        heapq.heappush(self.l,val)

        print(self.l,heapq.nlargest(3,self.l))
       
        return heapq.nlargest(self.k,self.l)[self.k-1]
