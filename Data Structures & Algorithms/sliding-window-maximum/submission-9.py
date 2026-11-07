from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        l = 0
        res = []     
        r = 0    
        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                
                q.pop()
            q.append(r)
            
            if r - l + 1 == k:
          
                res.append(nums[q[0]])
                while q and l >= q[0]:
                    q.popleft()
                l+=1
                r+=1
            else:
                r += 1
        return res
