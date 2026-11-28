class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)
        time = 0
        q = deque()
        while maxheap or q:
            time += 1
           
            if maxheap:
                c = heapq.heappop(maxheap)
                if c+1:
                    q.append([c+1,time+n])
         
            
            if q and q[0][1] == time:
                p = q.popleft()
                heapq.heappush(maxheap,p[0])
          
           

        return time

#time: O(m) we ignore n+1 because n is constant;space:O(1) because we have only 26 characters